import pymongo

uri = "mongodb+srv://avlyn:root@cluster0.i8iwrmi.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
db = client['gw2023pds1']
collections = db.list_collection_names()
for collection in collections:
    print(collection)

documents = db['customer'].find()
for document in documents:
    print(document)