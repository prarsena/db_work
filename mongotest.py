import pymongo
import datetime
import time
# Ensure you have a running mongodb server connection 
# to create the client for the mongoDB instance:
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

def getDatabaseNames():
    for db in client.list_databases():
        print(db)

def displayDBCollections():
    dbname = input("Enter new or existing db name: ")
    collection = client[dbname]
    return collection

getDatabaseNames()

def viewDocumentsInCollection():
    dbname = displayDBCollections()
    print(dbname.list_collection_names())
    collection = input("Enter new or existing collection name: ")
    print()
    documents = dbname[collection]
    for document in documents.find({}):
        print(document)

    return documents
    
def insertDocumentIntoCollection():
    print()
    collectionName = viewDocumentsInCollection()
    
    print("Number of documents in collection: ", collectionName.count_documents({}))
    print()
    print("Add Document to Collection:")
    name = input("     Enter your name: ")
    job = input("     Enter your job title: ")
    location = input("     Enter your location: ")
    startTime = time.time()
        
    testdocument = { "_id" : collectionName.count_documents({}) + 1, 
                "name" : name,
                "job" : job,
                "location": location,
                "date" : datetime.datetime.utcnow()}
    
    collectionName.insert_one(testdocument)

    print()
    for documents in collectionName.find({}):
        print(documents)

    print("Number of documents in collection: ", collectionName.count_documents({}))
    print ('This script took {0} seconds!'.format(time.time() - startTime))

insertDocumentIntoCollection()

# def menu:
#     choice = input("Type db names for a list of dbs on the mongo server")
#     if (choice == 'db'):
#         getDatabaseNames()