from flask import Flask, jsonify, request, render_template
import json
import datetime
import sqlite3#tables are sensors and triggers

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
    with sqlite3.connect("database.db") as connect:
        cursor = connect.cursor()
        triggers = cursor.execute("select * from triggers;")
        trigger_list = []

        for trigger_subList in triggers:
            triggerList = []
            for trigger in trigger_subList:
                triggerList.append(trigger)
                print(f"trigerlist:  {triggerList}")
            trigger_list.append(triggerList)
    with sqlite3.connect("database.db") as connect:
        cursor = connect.cursor()
        sensors = cursor.execute("select * from sensors;")
        sensor_list = []

        for sensor_subList in sensors:
            sensorList = []
            for sensor in sensor_subList:
                sensorList.append(sensor)
                print(f"trigerlist:  {sensorList}")
            sensor_list.append(sensorList)
    return(render_template("events.html", table = sensor_list)+render_template("events.html", table = trigger_list))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    