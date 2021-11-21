import os
import yaml
import pandas as pd
# import datetime
# import logging
# import requests
import json
# import csv
# import azure.functions as func
from azure.storage.blob import BlobServiceClient

class RandomUserClient:
    def __init__(self):
        self.setup()

    def load_config(self,dir_root):
        with open(dir_root + "/configs/azure_configs.yaml","r") as yamlfile:
            return yaml.load(yamlfile, Loader=yaml.FullLoader)

    def setup(self):
        dir_root = os.path.dirname(os.path.abspath(__file__))
        self.config = self.load_config(dir_root)
        blob_client = BlobServiceClient.from_connection_string(
            self.config['azure_storage_conn_str']).get_blob_client(self.config['container_name'], blob=f"data.json")
        with open('./data/data.json', "wb") as my_blob:
            blob_data = blob_client.download_blob()
            blob_data.readinto(my_blob)
        self.df = pd.read_json('./data/data.json')

    def get_users(self,query):
        return json.loads(self.df.to_json(orient='records'))