from flask import Flask, jsonify, request
import json
import datetime
import sqlite3#tables are sensors and triggers

connect = sqlite3.connect('database.db',check_same_thread=False)# format, check thead would make it error out becuse its sends back at different theread
cursor = connect.cursor()
app = Flask(__name__)

#try to accses or initalise tables
connect.execute(
    '''create table if not exists sensors (
    SENSORID int IDENTITY(1,1) PRIMARY KEY,
    NAME varchar(255) NOT NULL,
    TYPE varchar(255)
    );'''
)
connect.execute(
    '''create table if not exists triggers (
EVENTID int IDENTITY(1,1) PRIMARY KEY,
TIME DATETIME,
SENSORID int,
CONSTRAINT fk_sensor
FOREIGN KEY (SENSORID)
REFERENCES sensors(SENSORID)
);'''
)


@app.route('/api/data', methods=['POST'])
def receive_data():
    print("fish")
    data = request.json
    print("Received data from Feather:", data)
    date = datetime.datetime.now()
    sid = connect.execute("select SENSORID, SENSORID from triggers, sensors;")
    command = f"insert into triggers values({date},{data["ID"]});"
    cursor.execute(command)
    print(command)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    