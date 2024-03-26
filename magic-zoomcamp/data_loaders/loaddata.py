import argparse

# import pyspark
# from pyspark.sql import SparkSession
# from pyspark.conf import SparkConf
# from pyspark.context import SparkContext
# import os
# from pyspark.sql import functions as F
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



credentials_location = '/home/src/gcp/modern-tangent-413310-831bb8d92013.json'





@data_loader
def load_data(*args, **kwargs):

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
    # Specify your data loading logic here
    
    # spark = SparkSession.builder \
    # .config(conf=sc.getConf()) \
    # .getOrCreate()

    # df_index_spk= spark.read \
    #     .option("header", "true") \
    #     .csv(kwargs.get('input_path'))
    pd_csv = pd.read_csv(kwargs.get('input_path')) 
    return pd_csv 


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
