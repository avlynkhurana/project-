from session18a import *
from session18b import *
from bson.objectid import ObjectId

def main():
    db = MongoDBHelper()

    #customer = Customer()
    #customer.read_customer_data()

    #document = vars(customer)
    #db.insert(document)

    #db = MongoDBHelper()
    #customer = Customer()
    #customer.read_customer_data()

    #document = vars(customer)
    #db.insert(document)

    #query = {'phone': '99999 22222'}
    #query = {'email':'george@example.com'}
    query = {'_id':ObjectId('64c36c148675eb5d9c082ee2')}
    #db.delete(query)
    #db.fetch()
    db.fetch(query=query)

    document_data_to_update = {'name':'george w','phone':'99999 55555','age':33}
    db.update(document_data_to_update,query)


main()