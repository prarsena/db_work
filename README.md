# db_work
### Working with databases: sqlite, MongoDB

**sqlite3** is a library that is built-in with Python 3. It's a serverless database. 
The `sqlite.py` file is a fun little shell-based menu that allows you to add users
to the "Employee" table (it pre-loads 29 entries before you add your first user).
If you select "L" for Login, you are prompted to match a username with a password.
If you get a match, you can enter a message, which is posted to the "Messages" table.
You can then view messages using the 'M' key.

**MongoDB** is a NoSQL, schema-less database server that uses JSON-like documents as its records.
In this paradigm: A 'document' is like a record. A 'collection' is like a table.
MongoDB is used in Node applications as a part of the MEAN (or MERN, or MEVN) stack.
But to get familiar with this technology, I started off with just the mongo shell
and the Python MongoDB-driver, pymongo. With these two methods of accessing the 
Mongo server, I learned some of the basics of the technology. 

The `mongotest.py` file lets you view the existing databases, or create a database,
on your mongo server (default entry point: "mongodb://127.0.0.1:27017/").
After you select or create a database, you can access or create a collection 
in the database. Whether you access or create a collection, you are prompted to 
add a new document to the collection. The draw-back of this is that the database
schema is static with just the "name", "job", "location", and "date" fields.
After you add an entry, all documents in the collection are printed to the console.
