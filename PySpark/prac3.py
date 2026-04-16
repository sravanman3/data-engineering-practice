import os
import sys
from pyspark.sql import SparkSession
import pyspark.sql.functions as F

print("Python used by script:", sys.executable)

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder \
    .appName("practice") \
    .master("local[*]") \
    .getOrCreate()


data = [
    (1, "Alice", 25, 50000, "HR"),
    (2, "Bob", None, 30000, "IT"),
    (3, "Charlie", 30, None, "IT"),
    (4, "David", 22, 45000, None),
    (5, "Eve", -5, 70000, "HR"),
    (6, "Frank", 28, None, "Finance"),
    (7, "Grace", None, 52000, "Finance"),
    (8, "Hank", 35, 80000, "IT"),
    (9, "Ivy", 29, None, None),
    (10, "Jack", 40, 90000, "Finance")
]
columns = ["emp_id", "name", "age", "salary", "department"]

df = spark.createDataFrame(data, columns)

df_cleaned_age = df.withColumn("age",F.when(F.col("age")<0, F.lit(None)).otherwise(F.col("age")))
mean_age = df_cleaned_age.agg(F.mean("age").alias("mean_age")).collect()[0][0]
df_mean_age = df_cleaned_age.fillna({"age": mean_age})
df_mean_age.show()

## not sure which one is better so writing both
median_salary = df_mean_age.agg(F.median("salary").alias("median_salary")).collect()[0][0]
print(median_salary)
med_salary = df_mean_age.select(F.percentile_approx(F.col("salary"),0.5).alias("med_salary")).collect()[0][0]
print(med_salary)

df_med_salary = df_mean_age.fillna({"salary": med_salary})
df_med_salary.show()

mode_dept = (df_med_salary.filter(F.col("department").isNotNull())
             .groupBy("department")
             .count()
             .orderBy(F.desc("count"))
             .limit(1)).collect()[0]["department"]
df_mode_dept = df_med_salary.fillna({"department":mode_dept})
df_mode_dept.show()

df_filtered_data = df_mode_dept.filter((F.col("age")<35) & (F.col("salary")>40000))
df_filtered_data.show()

df_dept_summary = (df_filtered_data.groupBy("department")
                   .agg(F.count("*").alias("count_by_dept"),
                        F.avg("age").alias("avg_age_by_dept"),
                        F.avg("salary").alias("avg_salary_by_dept"),
                        F.min("salary").alias("min_salary"),
                        F.max("salary").alias("max_salary")).orderBy(F.desc("avg_salary_by_dept")))
df_dept_summary.show()

df.filter((F.col("age")<0) | (F.col("age").isNull())).show()
df.filter(F.col("salary").isNull()).show()
df.filter(F.col("department").isNull()).show()