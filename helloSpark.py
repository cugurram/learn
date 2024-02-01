from pyspark.sql import *


if __name__ == "__main__":
   spark = SparkSession.builder \
           .appName("HelloSpark") \
           .master("local[2]") \
           .getOrCreate()

   l = [("Ram", 23), ("Jake", 34), ("Sam", 56)]
   df = spark.createDataFrame(l).toDF("Name", "Age")
   df.show(2)
