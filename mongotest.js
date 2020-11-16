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

/*
// understand mongodb auth:
db = db.getSiblingDB('admin');
db.createUser(
    {
        user: "myUserAdmin",
        pwd: "password", // or cleartext password
        roles: [{ role: "userAdminAnyDatabase", db: "admin" }, "readWriteAnyDatabase"]
    }
)


db = db.getSiblingDB('reporting');
db.createUser({
    user: "reportsUser",
    pwd: "password",
    roles: [
        { role: "read", db: "test" },
        { role: "read", db: "reporting" },
        { role: "readWrite", db: "new_test_db" }
    ]
})
*/