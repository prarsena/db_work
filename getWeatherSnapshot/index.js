const mongo = require('mongodb');
const fetch = require('node-fetch');
const appkey = require('./api_key.js')
const MongoClient = mongo.MongoClient;

const url = 'mongodb://localhost:27017';
const api_key = appkey.mysecretkey;
const uri = `https://api.openweathermap.org/data/2.5/onecall?lat=42.36&lon=-71.07&exclude=minutely,hourly,daily&units=imperial&appid=${api_key}`
async function fetchWeather() {
    try {
        const response = await fetch(uri);
        const weather = await response.json()
        return weather;
    } catch (error) {
        console.log("Web service not returning data");
    }
}

// insert "weather snapshot" record into collection 
const client = new MongoClient(url, { useUnifiedTopology: true });
async function run() {
    try {
        await client.connect();
        const database = client.db("weatherDB");
        const collection = database.collection("weatherCollection");

        let ordered_id = await collection.estimatedDocumentCount()
        let weather = await fetchWeather()

        let date = weather.current.dt;
        let local_date = new Date((date) * 1000).toLocaleDateString("en-US");
        let local_time = new Date((date) * 1000).toLocaleTimeString("en-US");
        let sunrise = weather.current.sunrise;
        let local_sunrise = new Date((sunrise) * 1000).toLocaleTimeString("en-US");
        let sunset = weather.current.sunset;
        let local_sunset = new Date((sunset) * 1000).toLocaleTimeString("en-US");
        let current_temp = weather.current.temp;
        let feels_like = weather.current.feels_like;
        let weather_desc = weather.current.weather[0].description;

        //const doc = { _id: ordered_id + 1, date: local_date, time: local_time, sunrise: local_sunrise, sunset: local_sunset, temp: current_temp, feel: feels_like, description: weather_desc }
        const doc = { _id: ordered_id + 1, date: local_date, time: local_time, temp: current_temp, feel: feels_like, description: weather_desc }
        const addToCollection = await collection.insertOne(doc);
        addToCollection;

        if (addToCollection.insertedCount == 1) {
            console.log(`document added to collection`)
        } else {
            console.log(`something went wrong`)
        }

        const options = {
            sort: { time: 1 },
            projection: { _id: 0, date: 1, time: 1, sunrise: 1, sunset: 1, temp: 1, feel: 1, description: 1 },
        };

        /* query the collection */
        // return all results
        // const cursor = collection.find({}, options);
        // return latest result
        const cursor = collection.find({ _id: ordered_id + 1 }, options);
        if ((await cursor.count()) === 0) {
            console.log("No documents found!");
        }
        await cursor.forEach(console.dir);

    } catch (error) {
        throw error
    } finally {
        await client.close();
    }
}
run().catch(console.dir);