### Module_10_Sqlalchemy_Challenge

### Instructions

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

### Part 1: Analyse and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

Note that you’ll use the provided files (climate_starter.ipynb and hawaii.sqlite) to complete your climate analysis and data exploration.

Use the SQLAlchemy create_engine() function to connect to your SQLite database.

Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement.

Link Python to the database by creating a SQLAlchemy session.

Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.

Precipitation Analysis
Find the most recent date in the dataset.

Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.

![image](https://github.com/Dusko2779/BootCamp_sqlalchemy_challenge/assets/134830906/86a9fdb9-a3bc-4dde-bdfe-ae4d8f8e0720)


### Station Analysis
Design a query to calculate the total number of stations in the dataset.

Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:

![image](https://github.com/Dusko2779/BootCamp_sqlalchemy_challenge/assets/134830906/b81e284f-1e46-4afd-b9d4-ff1a8e0d00fd)

Answer the following question: which station id has the greatest number of observations?

Using the most-active station id, calculate the lowest, highest, and average temperatures.

Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:

Filter by the station that has the greatest number of observations.

Query the previous 12 months of TOBS data for that station.


![image](https://github.com/Dusko2779/BootCamp_sqlalchemy_challenge/assets/134830906/9689eee1-fef4-4c9b-b584-ea4add13f13d)


### Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

Start at the homepage.

List all the available routes.

/api/v1.0/precipitation
Convert the query results to a dictionary by using date as the key and prcp as the value.

Return the JSON representation of your dictionary.

/api/v1.0/stations
Return a JSON list of stations from the dataset.
/api/v1.0/tobs
Query the dates and temperature observations of the most-active station for the previous year of data.

![image](https://github.com/Dusko2779/BootCamp_sqlalchemy_challenge/assets/134830906/fb00abf4-7494-4b75-9701-117015e1132a)


Return a JSON list of temperature observations for the previous year.

/api/v1.0/<start> and /api/v1.0/<start>/<end>
Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

![image](https://github.com/Dusko2779/BootCamp_sqlalchemy_challenge/assets/134830906/b64ae713-e2e0-4627-999a-9a42c2fb220c)


For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

Hints
Join the station and measurement tables for some of the queries.

Use the Flask jsonify function to convert your API data to a valid JSON response object.
