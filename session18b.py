import pymongo
from tabulate import tabulate

class MongoDBHelper:

    def __init__(self,collection = 'customer'):
        uri = "mongodb+srv://avlyn:root@cluster0.i8iwrmi.mongodb.net/?retryWrites=true&w=majority"
        client = pymongo.MongoClient(uri)
        self.db = client['gw2023pds1']
        self.collection = self.db[collection]
        print("MongoDB Connected")

    def insert(self,document):
        result = self.collection.insert_one(document)
        print("Document Inserted:",result)

    def delete(self,query):
        result = self.collection.delete_one(query)
        print("Document Deleted:",result)

    def fetch(self,query =""):
        documents = self.collection.find(query)
        return list(documents)
        # for document in documents:
        #     print(document)
        # print(tabulate(documents,headers='keys'))

    def update(self,document,query):
        update_query = {'$set':document}
        result = self.collection.update_one(query,update_query)
        print("Updated document:",result.modified_count)
