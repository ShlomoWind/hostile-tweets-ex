import os
from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.user = os.getenv("USERNAME")
        self.password = os.getenv("PASSWORD")
        self.db_name = os.getenv("DB_NAME")
        self.col_name = os.getenv("COLLECTION_NAME")
        self.mongo_url = os.getenv("MONGO_URL")
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.col_name]

    def get_all_data(self):
        return list(self.collection.find({}))