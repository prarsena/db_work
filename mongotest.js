// mongo js file to be run in the mongo shell. 
db = new Mongo("localhost:27017").getDB("new_test_db");
collection = db.getCollection("new_test_collection");

print("Names of collections in database:")
print(db.getCollectionNames());

if (collection.count() < 5) {
    id = collection.count() + 1;
    collection.insert({
        "_id": id,
        "name": "James Ken",
        "Occupation": "Police Chief"
    });
}

cursor = collection.find();
while (cursor.hasNext()) {
    printjson(cursor.next());
}

print("Number of documents in " + collection.getFullName() + ": " + collection.count());


/* note for the documentation:
https://docs.mongodb.com/manual/tutorial/write-scripts-for-the-mongo-shell/
for the load("path/to/file.js")
the mongo shell does not support the Windows-style (backslash)
filepaths. You must use forward slashes to specify the filepath
even on Windows.
*/

/*  I notice when I add an "_id" field,
    the printjson spits out something that isn't formatted like
    the output present when I don't specify the "_id" field

> load("D:/Sandbox/py/db_work/mongotest.js")
Names of collections in database:
new_test_collection
{ "_id" : 1, "name" : "James Ken", "Occupation" : "Police Chief" }
{ "_id" : 2, "name" : "James Ken", "Occupation" : "Police Chief" }
{ "_id" : 3, "name" : "James Ken", "Occupation" : "Police Chief" }
{ "_id" : 4, "name" : "James Ken", "Occupation" : "Police Chief" }
{ "_id" : 5, "name" : "James Ken", "Occupation" : "Police Chief" }
Number of documents in new_test_db.new_test_collection: 5
true

> db.dropDatabase()
{ "dropped" : "new_test_db", "ok" : 1 }

> load("D:/Sandbox/py/db_work/mongotest.js")
Names of collections in database:
{
        "_id" : ObjectId("5f3dd268a4210146578af536"),
        "name" : "James Ken",
        "Occupation" : "Police Chief"
}
Number of documents in new_test_db.new_test_collection: 1
true
*/