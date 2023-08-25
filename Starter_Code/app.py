# Import necessary libraries
from flask import Flask, jsonify
import datetime as dt
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import numpy as np  

# Create an instance of Flask
app = Flask(__name__)

# Create an engine to connect to the SQLite database
engine = create_engine("sqlite:///Starter_Code/Resources/hawaii.sqlite")

# Reflect the database tables into classes using automap_base()
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to the classes named "station" and "measurement"
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create a session
session = Session(engine)
#########################################################################################################################
# Define the homepage route to list available routes
@app.route("/")
def home():
    return (
        "Welcome to the Climate App API! List of available routes:\n"
        "/api/v1.0/precipitation\n"
        "/api/v1.0/stations\n"
        "/api/v1.0/tobs\n"
        "/api/v1.0/<start>\n"  
        "/api/v1.0/<start>/<end>\n"
    )
########################################################################################################################
# Define the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Query to retrieve precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()

    # Convert the query results to a dictionary with date as the key and prcp as the value
    precipitation_data = {date: prcp for date, prcp in results}

    return jsonify(precipitation_data)
#######################################################################################################################
# Define the /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def stations():
    # Create a new session
    session = Session(engine)

    # Query to retrieve station data
    results = session.query(Station.station).all()

    # Convert the query results to a list
    station_list = list(np.ravel(results))

    # Close the session
    session.close()

    return jsonify(station_list)

#####################################################################################################################

# Define the /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    # Get the most active station ID from a previous query
    most_active_station = "USC00519281"
    
    # Calculate the date one year from the last date in the dataset
    last_date = session.query(func.max(Measurement.date)).scalar()
    one_year_ago = dt.datetime.strptime(last_date, "%Y-%m-%d") - dt.timedelta(days=365)

    # Query to retrieve temperature data for the most active station and the last year
    results = session.query(Measurement.date, Measurement.tobs)\
        .filter(Measurement.station == most_active_station)\
        .filter(Measurement.date >= one_year_ago).all()

    # Convert the query results to a list of dictionaries
    tobs_list = [{"date": date, "temperature": tobs} for date, tobs in results]

    return jsonify(tobs_list)


###############################################################################################################

# Define the /api/v1.0/<start> route
@app.route("/api/v1.0/<start>")
def temp_range_start(start):
    try:
        # Convert the start date to a datetime object
        start_date = dt.datetime.strptime(start, '%Y-%m-%d')

        # Create a new session
        session = Session(engine)

        # Query to calculate temperature statistics for dates greater than or equal to the start date
        temperature_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date).all()

        # Convert the query results to a dictionary
        temp_stats_dict = {
            "TMIN": temperature_stats[0][0],
            "TAVG": temperature_stats[0][1],
            "TMAX": temperature_stats[0][2]
        }

        return jsonify(temp_stats_dict)
    except Exception as e:
        # Handle exceptions if needed
        return jsonify({"error": str(e)})
    finally:
        # Make sure to close the session even if there's an exception
        if session:
            session.close()

# Define the /api/v1.0/<start>/<end> route
@app.route("/api/v1.0/<start>/<end>")
def temp_range_start_end(start, end):
    try:
        # Convert the start and end dates to datetime objects
        start_date = dt.datetime.strptime(start, '%Y-%m-%d')
        end_date = dt.datetime.strptime(end, '%Y-%m-%d')

        # Create a new session
        session = Session(engine)

        # Query to calculate temperature statistics for dates between start and end dates
        temperature_stats = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))\
            .filter(Measurement.date >= start_date)\
            .filter(Measurement.date <= end_date).all()

        # Convert the query results to a dictionary
        temp_stats_dict = {
            "TMIN": temperature_stats[0][0],
            "TAVG": temperature_stats[0][1],
            "TMAX": temperature_stats[0][2]
        }

        return jsonify(temp_stats_dict)
    except Exception as e:
        # Handle exceptions if needed
        return jsonify({"error": str(e)})
    finally:
        # Make sure to close the session even if there's an exception
        if session:
            session.close()

if __name__ == "__main__":
    app.run(debug=True)