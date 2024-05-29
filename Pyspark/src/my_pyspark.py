import pandas
import pyspark
from pyspark.sql import SparkSession

print(SparkSession._instantiatedSession)
if SparkSession._instantiatedSession is not None:
    SparkSession._instantiatedSession.stop()

spark = SparkSession.builder.appName("Practise").getOrCreate()
spark
df = spark.read.csv("pyspark_data.csv")
df.show()
df_pyspark = spark.read.option("header", "true").csv(
    "pyspark_data.csv", inferSchema=True
)
# if inferSchema is False, it will assume all the features as string
df_pyspark
type(df_pyspark)
df_pyspark.head(3)
df_pyspark.printSchema()
df_pyspark.columns
df_pyspark.select("name").show()
df_pyspark.select(["name", "age"]).show()
df_pyspark.dtypes
df_pyspark.describe().show()
# Adding columns
df_pyspark = df_pyspark.withColumn("blabla", df_pyspark["age"] + 2)
df_pyspark.show()
# Drop the column
df_pyspark = df_pyspark.drop("blabla")
df_pyspark.show()
# Rename columns
df_pyspark = df_pyspark.withColumnRenamed("name", "Name")
df_pyspark = spark.read.option("header", "true").csv(
    "pyspark_data_na.csv", inferSchema=True
)
# Dropping NA values
df_pyspark.na.drop().show()
df_pyspark.na.drop(how="all").show()  # 'any' by default
# Threshold
df_pyspark.na.drop(thresh=3).show()  # minimum value of non-null values
# Subset
df_pyspark.na.drop(
    subset=["job"]
).show()  # select column where you want to remove null values
# Fill missing values
df_pyspark.na.fill(value="Missing Value").show()
df_pyspark.na.fill(value="Missing Value", subset=["age"]).show()
from pyspark.ml.feature import Imputer

imputer = Imputer(
    inputCols=["age"], outputCols=["{}_imputed".format(c) for c in ["age"]]
).setStrategy("median")
imputer.fit(df_pyspark).transform(df_pyspark).show()
# Filtering
df_pyspark.filter("age<8").show()
df_pyspark.filter("age<8").select(["name", "age"]).show()
df_pyspark.filter(df_pyspark["age"] < 8).show()
df_pyspark.filter((df_pyspark["age"] < 8) & (df_pyspark["age"] > 3)).show()
df_pyspark.filter((df_pyspark["age"] > 8) | (df_pyspark["age"] < 3)).show()
df_pyspark.filter(~(df_pyspark["age"] < 8)).show()
# GroupBy
df_pyspark.groupBy("job").sum().show()
df_pyspark.groupBy("job").mean().show()
df_pyspark.groupBy("job").count().show()
df_pyspark.agg({"age": "sum"}).show()
