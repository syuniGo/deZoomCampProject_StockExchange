if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from pyspark.sql import types
import pandas as pd


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



@transformer
def transform(data, *args, **kwargs):
    data.info
    schema = {
        'Index': str,
        # 'Date': 'datetime64[ns]',        
        'Open': float,
        'High': float,
        'Low': float,
        'Close': float,
        'Adj Close': float,
        'Volume': int,
        'CloseUSD' : float
    }
        # 找到包含 'null' 的行
    # null_rows_before = data.eq('null').any(axis=1)

    # 替换 'null'


    # null_rows = data.isnull().any(axis=1)
    # print('null',data.isnull().sum())
    # print('null', data[null_rows])
    # data = data.replace('null', 0)

    data = data.astype(schema)
    pd.to_datetime(data['Date'])

    data.info
    

    print(args)



    # # 再次找到包含 'null' 的行
    # null_rows_after = data.eq('null').any(axis=1)

    # # 找出被替换的行
    # changed_rows = null_rows_before & ~null_rows_after

    # # 显示被替换的行
    # print(data[changed_rows])


    # spark = kwargs.get('spark')
    # df_green2 = spark.read \
    # .option("header", "true") \
    # .csv('gs://ny_taxi_dbt101/taxi_zone_lookup.csv')
    # df_green2.show()
    # Specify your transformation logic here

    return data


@test
def test_output(output, *args) -> None:
    output.info
    """
    Template code for testing the output of the block.
    """
    print('test', args)

    assert output is not None, 'The output is undefined'
