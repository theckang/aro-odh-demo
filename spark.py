# PYSPARK_SUBMIT_ARGS
# --conf spark.cores.max=2 --conf spark.executor.instances=2 --conf spark.executor.memory=1G --conf spark.executor.cores=1 --conf spark.driver.memory=2G --packages org.apache.hadoop:hadoop-azure:3.2.1,org.apache.hadoop:hadoop-azure-datalake:3.2.1 pyspark-shell

import os
from pyspark.sql import SparkSession

# create a spark session
spark_cluster_url = f"spark://{os.environ['SPARK_CLUSTER']}:7077"
spark = SparkSession.builder.master(spark_cluster_url).getOrCreate()

spark = SparkSession \
    .builder \
    .master(spark_cluster_url) \
    .config("spark.hadoop.fs.azure.account.auth.type", "OAuth") \
    .config("spark.hadoop.fs.azure.account.oauth.provider.type", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider") \
    .config("spark.hadoop.fs.azure.account.oauth2.client.id", "") \
    .config("spark.hadoop.fs.azure.account.oauth2.client.secret", "") \
    .config("spark.hadoop.fs.azure.account.oauth2.client.endpoint", "https://login.microsoftonline.com/<tenant-id>/oauth2/token") \
    .config("spark.hadoop.fs.azure.createRemoteFileSystemDuringInitialization", "true") \
    .getOrCreate()

data = "abfss://mycontainer@datalake555.dfs.core.windows.net/iris.data"
df = spark.read.load(data)
df.show()
