getWeatherSnapshot is a node.js application that uses `node-fetch` and `mongodb` to fetch current weather information from `openweathermap.org`.
The application then writes the current weather information (a weather "snapshot") to a Mongo DB collection (db: `weatherDB`; collection: `weatherCollection`).

# How to run the application

### Prerequisites

1. Create an account on [Open Weather Map] (https://openweathermap.org/api) to obtain an API key. This is free for personal use. The API key will be sent in an email from openweathermap. It can take up to an hour before the key is active.

- Test the status of your API key by entering the following in a web browser: https://api.openweathermap.org/data/2.5/onecall?lat=42.36&lon=-71.07&exclude=minutely,hourly,daily&units=imperial&appid={your_api_key}.

2. Clone this repository to your local environment.
3. In your local environment, create a file in the same directory as `index.js` called `api_key.js` with the following text:

   const mysecretkey = "<i>enter_secret_key_here</i>";
   module.exports = { mysecretkey }

4. Ensure your Mongo DB instance is running! This program uses the default instance location: `mongodb://localhost:27017`.

### Build the project and run

1. In a terminal, build the project dependencies:

   ```
   > npm install index.js
   ```

2. Run the index.js file:

   ```
   > node index.js
   ```

3. Use the mongo shell to verify the document was added to the collection:

   ```
   >use weatherDB
   switched to db weatherDB
   >db.weatherCollection.count()
   1
   >db.weatherCollection.find({})
   { "\_id" : 1, "date" : "11/15/2020", "time" : "11:41:08 PM", "temp" : 55.65, "feel" : 41.38, "description" : "mist" }
   ```

### Notes and Next steps

The `lat` and `lon` fields in the `uri` variable are set to Boston Logan Airport by default, but should be tailored to fit the geographic region you want data for.

There are several variables defined that we haven't used yet which can be added to the document. In fact, the `onecall` api has many more fields that can be used to capture a "weather snapshot".
See the openweathermap documentation for more information: https://openweathermap.org/api/one-call-api

Next steps for this project:

- Add this application logic to a server using either the `http` or `express` modules.
- Set the app to run on a schedule using a chron job (possibly using `chrontab`) to collect hourly weather data.
- Run application in a Docker container.
- Use the collected data to build visualizations (temperature visualization)
- Use this app logic with any API that returns data that changes! (for example: track prices)
