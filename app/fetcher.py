import os
from pymongo import MongoClient

class Connection:
    def __init__(self):
        self.user = os.getenv("USERNAME","IRGC")
        self.password = os.getenv("PASSWORD","iraniraniran")
        self.db_name = os.getenv("DB_NAME","IranMalDB")
        self.col_name = os.getenv("COLLECTION_NAME","tweets")
        self.mongo_url = os.getenv("MONGO_URL","mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/")
        self.client = MongoClient(self.mongo_url)
        self.db = self.client[self.db_name]
        self.collection = self.db[self.col_name]

    def get_all_data(self):
        return list(self.collection.find({}))