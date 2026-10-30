from flask import Flask, jsonify, request, render_template
import json
import datetime
import sqlite3#tables are sensors and triggers
from pages import *

connect = sqlite3.connect('database.db')# format, check thead would make it error out becuse its sends back at different theread
cursor = connect.cursor()
app = Flask(__name__)

#try to accses or initalise tables
connect.execute(
    '''create table if not exists sensors (
    SENSORID INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME varchar(255) NOT NULL,
    TYPE varchar(255)
    );'''
)
connect.execute(
    '''create table if not exists triggers (
EVENTID INTEGER PRIMARY KEY AUTOINCREMENT,
TIME DATETIME,
SENSORID int,
CONSTRAINT fk_sensor
FOREIGN KEY (SENSORID)
REFERENCES sensors(SENSORID)
);'''
)


@app.route('/api/data', methods=['POST'])
def receive_data():

    data = request.json
    print("Received data from Feather:", data)
    date = datetime.datetime.now()
    with sqlite3.connect("database.db") as connect:
        command = f"insert into triggers(TIME, SENSORID) values('{date}','{data["ID"]}');"
        cursor = connect.cursor()
        print(command)
        print(cursor.execute(command))
        print(command)
    return jsonify({"status": "success", "received": data}), 200

@app.route('/')
def home():
    sensor = render_template("events.html", table = event("sensors"))
    trigger = render_template("events.html", table = event("triggers"))
    index = render_template("index.html")
    return(index+sensor + trigger)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    