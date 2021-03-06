# db_work

### Working with databases: sqlite, MongoDB

**sqlite3** is a library that is built-in with Python 3. It's a serverless database.

- The `sqlite.py` file is a shell-based menu script that allows you to add users
  to the "Employee" table (it pre-loads 29 entries before you add your first user).
  If you select "L" for Login, you are prompted to match a username with a password.
  If you get a match, you can enter a message, which is posted to the "Messages" table.
  You can then view messages using the 'M' key.

**MongoDB** is a NoSQL, flexible schema database server that uses JSON-like documents as its records.
In this paradigm: A 'document' is like a record. A 'collection' is like a table.
MongoDB is used in Node applications as a part of the MEAN (or MERN, or MEVN) stack.
But to get familiar with this technology, I started off with just the mongo shell
and the Python MongoDB-driver, pymongo. With these two methods of accessing the
Mongo server, I learned some of the basics of the technology.

- The `mongotest.py` file lets you view the existing databases, or create a database,
  on your mongo server (default entry point: "mongodb://127.0.0.1:27017/").
  After you select or create a database, you can access or create a collection
  in the database. Whether you access or create a collection, you are prompted to
  add a new document to the collection. The draw-back of this is that the database
  schema is static with just the "name", "job", "location", and "date" fields.
  After you add an entry, all documents in the collection are printed to the console.

- The `mongotest.js` file explores running javascript in the mongo shell.
  The `mongotest.js` file establishes a connection to the mongo server,
  and creates the database, "new_test_db". It then adds five documents to the
  created collection, "new_test_collection", and then prints those documents
  to the console using a cursor object. This file is meant to be used with the
  mongo shell using the `>load("path/to/mongotest.js")` command.

The **getWeatherSnapshot** directory contains a Node.js project for getting weather data using `node-fetch`
and entering the information into a Mongo DB instance. See that project's README for more information.

The **mongodb_java_driver** project directory contains my work setting up the
MongoDB Java dependencies using Gradle. This was my first experience using Gradle
to manage dependencies, so hopefully I added all the necessary files to my GitHub Repo.
The `build.gradle` file fetches the dependencies from the `mavenCentral()` repo, and sets
some attributes for running the project.

- The `src/main/accessmongo/Main.java` file uses these dependencies from Gradle to use the
  MongoDB Java libraries. The `Main.java` file adds many users to a collection,
  and displays them to the console using a cursor object.
  Building the project should be as simple as typing `>gradle run` in the
  project root directory (`/monogdb_java_driver/`), assuming the database is running.
  This command displays the output to the console.

#### Troubleshooting the Mongo Server

Note: if you accidentally kill your mongoDB server,
ensure the database has a correct path, for example:

> mongod --dbpath "c:\Program Files\MongoDB\data"

Note: this command may need to be run as administrator.
or, if that doesn't work, use a CMD prompt with Administrator credentials:

    C:\WINDOWS\system32>net start MongoDB
    The MongoDB Server (MongoDB) service is starting.
    The MongoDB Server (MongoDB) service was started successfully.

Then verify it by typing "mongo" into the console
(assuming you have added mongo.exe to your PATH)
