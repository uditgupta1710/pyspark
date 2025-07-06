from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Example").getOrCreate()
#df = spark.createDataFrame([(1, 'Alice'), (2, 'Bob')], ['id', 'name'])
#df.show()

df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()