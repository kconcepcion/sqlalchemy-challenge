

# ###############################################
import pandas as pd
import numpy as np
import datetime as dt
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import flask
from flask import Flask , jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def homepage():
    return (f"Homepage <br/>"
           f"Available routes <br/>"
           f"/api/v1.0/precipitation <br/>"
           f"/api/v1.0/stations <br/>"
           f"/api/v1.0/tobs <br/>"
           f"/api/v1.0/start <br/>"
           f"/api/v1.0/temp/start/end")

def precipitation():
    precip_year = session.query(Measurement.prcp , Measurement.date).\
    filter(Measurement.date > '2016-08-23').\
    order_by(Measurement.date).all()
    precip = {date : x for date , x in precip_year}
    return jsonify(precip)

   
@app.route("/api/v1.0/stations")

def station():
    result = session.query(Station.station).all()
    stationlist = list(np.ravel(result))
    return jsonify (stationlist)
           
@app.route("/api/v1.0/tobs")

def tobs():
    Tobss = session.query(Measurement.tobs).\
            filter(Measurement.station == 'USC00519281' ).\
            filter(Measurement.date >= '2017,8,23').all()
    Tobslist = list(np.ravel(Tobss))
    return jsonify (Tobslist)

@app.route ("/api/v1.0/<start>")
def temps(start):
    startData = session.query(Measurement).filter(Measurement.date>= start)
    startList =[] 
    for row in startData:
        startList.append(row.tobs) 
    return (jsonify ({"tempmin": min(startList),"tempmax": max(startList),"tempavg":np.mean}))

@app.route ("/api/v1.0/<start>/<end>")

def Tempscalc(start,end):
    findings = session.query(Measurement).filter(Measurement.date>= start).filter(Measurement.date<=end)
    found =[] 
    for row in findings:
        found.append(row.tobs) 
    return (jsonify ({"tempmin": min(found),"tempmax": max(found),"tempavg":np.mean}))
           
if __name__ == '__main__':
    app.run(debug=True)




