import os
import sys
from pyspark.sql import SparkSession
import pyspark.sql.functions as F
# from pyspark.sql.functions import when

print("Python used by script:", sys.executable)

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder \
    .appName("practice") \
    .master("local[*]") \
    .getOrCreate()

data = [
    (1,"Alice", 25, 50000),
    (2,"Bob", None, 30000),
    (3,"Charlie", 30, None),
    (4,"David", 22, 45000),
    (5,"Eve",-5,70000)
]

columns = ["emp_id","name","age","salary"]

df = spark.createDataFrame(data,columns)
# df.printSchema()
# df.show()
#
# df.describe().show()
#
# df_cols=df.select(["name", "salary"])
# df_cols.show()
#
# df_cols=df.select(["emp_id","name","salary"])
# df_cols.show()
#
# df_c = df.select([col for col in df.columns if col != "age"])
# df_c.show()

df = df.withColumn("salary_in_k", F.col("salary")/1000)
df.show()

df = df.withColumn("age_category",F.when(F.col("age").isNull(),"Unknown")
                   .when(F.col("age")<0,"Invalid")
                   .when(F.col("age")<25,"Young")
                   .when((F.col("age")>=25) & (F.col("age")<30),"Adult")
                   # .when(F.col("age")>=30,"Senior")
                   .otherwise("Senior")
                   )
df.show()

df = df.withColumn("valid_age",F.when(F.col("age").isNull(),False)
                                        .when(F.col("age")<0,False)
                                        .otherwise(True))
df.show()

df.filter(F.col("valid_age") == True).show()
df.filter(F.col("salary").isNull()).show()
df.filter(F.col("age_category")=="Invalid").show()


# Valid employees with salary above 40k
df_valid_emp = df.filter((F.col("valid_age")) & (F.col("salary")>40000))
df_valid_emp.show()

# Employees with missing age or missing salary
df_miss_age_sal = df.filter((F.col("age").isNull()) | (F.col("salary").isNull()))
df_miss_age_sal.show()

# Employees who are either Young or Invalid
df_young_invalid = df.filter((F.col("age_category") == "Young") | (F.col("age_category") == "Invalid"))
df_young_invalid.show()
# OR
df_yound_invalid = df.filter(F.col("age_category").isin("Young","Invalid"))
df_yound_invalid.show()

df_final = df.select(F.col("emp_id"),
                     F.col("name"),
                     (F.col("salary")/1000).alias("salary_in_k"),
                     (F.when(F.col("age").isNull(),"Unknown")
                      .when(F.col("age")<0,"Invalid")
                      .when(F.col("age")<25,"Young")
                      .when((F.col("age")>=25) & (F.col("age")<30),"Adult")
                      .otherwise("Senior")).alias("age_category"),
                     (F.when(F.col("age").isNull(),False)
                      .when(F.col("age")<0,False)
                      .otherwise(True)).alias("valid_age")
                     )
df_final.show()

df_final_sal_asc = df_final.orderBy("salary_in_k")
df_final_sal_asc.show()

df_final_sal_desc = df_final.orderBy("salary_in_k", ascending=False)
df_final_sal_desc.show()

df_final.orderBy("age_category","salary_in_k").show()

df_final.orderBy("age_category", ascending=False).show()
df_final.orderBy("valid_age","salary_in_k", ascending=False).show()

df_final.orderBy(F.col("valid_age").desc(),
                 F.col("salary").asc()).show()
