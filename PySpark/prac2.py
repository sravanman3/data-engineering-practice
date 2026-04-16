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
    (1,"Alice", 25, 50000, "HR"),
    (2,"Bob", None, 30000, "IT"),
    (3,"Charlie", 30, None, "IT"),
    (4,"David", 22, 45000, None),
    (5,"Eve",-5,70000, "HR"),
    (6,"Frank", 28, None, "Finance"),
    (7,"Grace", None, 52000, "Finance"),
    (8,"Hank", 35, 80000, "IT"),
    (9,"Ivy", 29, None, None)
]

columns = ["emp_id","name","age","salary","department"]

df_spark = spark.createDataFrame(data, columns)

df_spark.show()
df_spark.where(df_spark["age"].isNull()).show() # tell me if there is another approach
df_spark.where(df_spark["salary"].isNull()).show()
df_spark.where(df_spark["department"].isNull()).show()

df_spark.filter(F.col("age").isNull()).show()
df_spark.filter(F.col("age").isNull() |
                F.col("salary").isNull() |
                F.col("department").isNull()).show()

df_spark.drop(df_spark["salary"].isNull()).show() ## not sure how to do, please guide
df_spark.dropna(subset=["salary"]).show()

df_spark.dropna(how="any").show()
df_spark.dropna(thresh=4).show() # drop rows where at least 2 values are null
df_spark.dropna(how="any",subset=["age","department"]).show()

df_spark.drop("department").show()

df_spark.select(F.avg("age")).show()
mean_age = df_spark.select(F.avg("age")).collect()[0][0]

df_filled = df_spark.fillna({"age": mean_age})
df_filled.show()

df_filled.filter(F.col("age")<0).show()

df_inv = df_spark.withColumn("age",F.when(F.col("age")<0, F.lit(None)).otherwise(F.col("age")))
df_inv.show()

mean_age = df_inv.select(F.avg("age")).collect()[0][0]
df_na = df_inv.fillna({"age": mean_age})
df_na.show()

# mean_salary = df_na.select(F.avg("salary")).collect()[0][0]
# print(mean_salary)
#
# df_salary = df_na.fillna({"salary": mean_salary})
# df_salary.show()

median_salary = df_na.select(F.percentile_approx("salary",0.5).alias("median_salary")).collect()[0][0]
print(median_salary)

df_sal_median = df_na.fillna({"salary": median_salary})
df_sal_median.show()

mode_dept = (df_sal_median.filter(F.col("department").isNotNull())
             .groupBy("department")
             .count()
             .orderBy(F.desc("count"))
             .limit(1)
             ).collect()[0]["department"]

df_dept_mode = df_sal_median.fillna({"department": mode_dept})
df_dept_mode.show()

df_dept_mode.groupBy("department").count().show()
df_dept_mode.groupBy("department").avg("salary").show()

df_dept_mode.groupBy("department").agg(F.avg("salary").alias("avg_sal_by_dept"),F.count("emp_id").alias("count")).show()
df_dept_mode.groupBy("department").agg(F.min("salary").alias("min_sal_by_dept"),F.max("salary").alias("max_sal_by_dept")).show()

df_summary_dept=(df_dept_mode.groupBy("department")
                 .agg(F.count("*").alias("count_by_dept"),
                      F.avg("salary").alias("avg_sal_by_dept"),
                      F.avg("age").alias("avg_age_by_dept"),
                      F.min("salary").alias("min_sal_by_dept"),
                      F.max("salary").alias("max_sal_by_dept")
                      )
                 .orderBy(F.desc("avg_sal_by_dept")))
df_summary_dept.show()

(df_dept_mode.filter(F.col("salary")>40000).groupBy("department").agg(F.count("*").alias("count_by_dept"),F.avg("salary").alias("avg_sal_by_dept"))).show()
df_dept_mode.filter(F.col("age")<30).groupBy("department").agg(F.count("*").alias("count_by_dept")).show()
df_dept_mode.filter(F.col("age")>0).groupBy("department").agg(F.avg("age").alias("avg_age_by_dept")).show()