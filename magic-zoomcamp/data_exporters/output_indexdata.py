from pyspark.sql import types

import pyspark
from pyspark.sql import SparkSession
from pyspark.conf import SparkConf
from pyspark.context import SparkContext
import os
from pyspark.sql import functions as F
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

schema = types.StructType([
    types.StructField('Index', types.StringType(), True), 
    types.StructField('Date', types.DateType(), True), 
    types.StructField('Open', types.DoubleType(), True), 
    types.StructField('High', types.DoubleType(), True), 
    types.StructField('Low', types.DoubleType(), True), 
    types.StructField('Close', types.DoubleType(), True), 
    types.StructField('Adj Close', types.DoubleType(), True), 
    types.StructField('Volume', types.IntegerType(), True)
])

credentials_location = '/home/src/gcp/modern-tangent-413310-831bb8d92013.json'


# conf = SparkConf() \
# .setMaster("local[*]") \
# .setAppName('test') \
# .set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
# .set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", credentials_location)

# sc = SparkContext.getOrCreate(conf=conf)
# hadoop_conf = sc._jsc.hadoopConfiguration()
# hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
# hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
# hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
# hadoop_conf.set("fs.gs.auth.service.account.enable", "true")
# # Specify your data loading logic here

# spark = SparkSession.builder \
# .config(conf=sc.getConf()) \
# .getOrCreate()


conf = SparkConf() \
.setMaster("local[*]") \
.setAppName('test') \
.set("spark.jars", "gcs-connector-hadoop3-2.2.5.jar") \
.set("spark.hadoop.google.cloud.auth.service.account.enable", "true") \
.set("spark.hadoop.google.cloud.auth.service.account.json.keyfile", credentials_location)

sc = SparkContext.getOrCreate(conf=conf)
hadoop_conf = sc._jsc.hadoopConfiguration()
hadoop_conf.set("fs.AbstractFileSystem.gs.impl",  "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFS")
hadoop_conf.set("fs.gs.impl", "com.google.cloud.hadoop.fs.gcs.GoogleHadoopFileSystem")
hadoop_conf.set("fs.gs.auth.service.account.json.keyfile", credentials_location)
hadoop_conf.set("fs.gs.auth.service.account.enable", "true")
# Specify your data loading logic here

spark = SparkSession.builder \
.config(conf=sc.getConf()) \
.getOrCreate()
print(spark)

@data_exporter
def export_data(data, *args, **kwargs):


    data
    df = data.groupby('Index')
    indexSet = df.groups.keys()
    print(indexSet)
    df_res = spark.createDataFrame(data)
    df_res.show()
    print(df_res.schema)
    output_path = kwargs.get('output_path')

    # 将pandas DataFrame转换为Spark DataFrame
    # spark_df = spark.createDataFrame(df)

    # 显示Spark DataFrame
    # spark_df.show()
    for index in indexSet:
        print(f'processing date for {index}')

        # df_r = spark.read \
        #     .option("header", "true") \
        #     .schema(schema)  \
        #     .csv(input_d) \
        df_result = df_res.filter(df_res.Index == index)
        
        df_result.show()
        
        df_result \
            .repartition(4) \
            .write \
            .parquet(f'{output_path}/{index}')

