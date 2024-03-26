from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Google Cloud Storage bucket.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#googlecloudstorage
    """
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = kwargs.get('output_path')
    input_csv = kwargs.get('indexInfo')

    df_indexInfo = pd.read_csv(input_csv)
    output = kwargs.get('indexInfo').split('/')[-2:]
    object_key = '/'.join(output)

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df_indexInfo,
        bucket_name,
        object_key
    )
