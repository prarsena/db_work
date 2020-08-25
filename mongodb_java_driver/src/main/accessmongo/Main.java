package accessmongo;

import com.mongodb.ConnectionString;
import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.ServerAddress;

import com.mongodb.client.MongoDatabase;
import com.mongodb.client.MongoCollection;

import org.bson.Document;
import java.util.Arrays;
import com.mongodb.Block;

import com.mongodb.client.MongoCursor;
import static com.mongodb.client.model.Filters.*;
import com.mongodb.client.result.DeleteResult;
import static com.mongodb.client.model.Updates.*;
import com.mongodb.client.result.UpdateResult;
import java.util.ArrayList;
import java.util.List;

public class Main {
   public static void main( String[] args ){
	System.out.println("Hello Mongo!");

	MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017");
	MongoDatabase database = mongoClient.getDatabase("java_test_db");
    MongoCollection<Document> collection = database.getCollection("java_test_collection");
    
    /* clear records from previous runs. */
    final Document deleteFilter = new Document("Name", "John Wick"); 
    DeleteResult deleteResult = collection.deleteMany(deleteFilter);
    DeleteResult singleResult = collection.deleteOne(eq("_id", 11));
    
    System.out.println("Previous documents deleted? " + deleteResult.wasAcknowledged() + ", " + singleResult.wasAcknowledged());

    /* Insert many users named John Wick into the java_test_collection */
    List<Document> documents = new ArrayList<Document>();
    for (int i = 1; i <= 10; i++) {
        if (i > 1) {
            documents.add(new Document("_id", i)
            .append("Name", "John Wick")
            .append("Profession", "Retired")
            .append("Salary", i + " Gold Coins"));
        }
        else { 
            documents.add(new Document("_id", i)
            .append("Name", "John Wick")
            .append("Profession", "Retired")
            .append("Salary", i + " Gold Coin"));
        }
    }
    collection.insertMany(documents);
    
    /* insert a single document into the collection */
    Document document = new Document("_id", 11)
                            .append("Name", "John Carpenter")
                            .append("Profession", "Director")
                            .append("Biography", new Document("Birthplace", "Carthage, NY").append("Birthdate", "Jan 16, 1948"))
                            .append("Films", Arrays.asList("Halloween", "The Thing", "Escape From New York"));
    
    collection.insertOne(document);
    
    /* Use a cursor object to iterate through the collection */
    System.out.println();
    System.out.println("Documents in the java_test_collection:");
    MongoCursor<Document> cursor = collection.find().iterator();
	try {
		while (cursor.hasNext()) {
			System.out.println(cursor.next().toJson());
		}
	} finally {
		cursor.close();
	}
    
    /* Test out other APIs */ 
    System.out.println();
	System.out.println("Number of records in collection: " + collection.countDocuments());
   }
}