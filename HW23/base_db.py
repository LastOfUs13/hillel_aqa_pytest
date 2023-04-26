import pymongo


class BaseDb:

    def __init__(self, database_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def my_insert_one(self, document):
        return self.collection.insert_one(document)

    def my_find_one(self, query):
        return self.collection.find_one(query)

    def my_insert_many(self, documents):
        return self.collection.insert_many(documents)

    def my_find(self):
        return self.collection.find()
