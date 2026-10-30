from flask import Flask, jsonify, request, render_template
import json
import datetime
import sqlite3#tables are sensors and triggers
database = "database.db"

def event(table):
    
    with sqlite3.connect("database.db") as connect:
        cursor = connect.cursor()
        sensors = cursor.execute(f"select * from {table};")
        sensor_list = []

        for sensor_subList in sensors:
            sensorList = []
            for sensor in sensor_subList:
                sensorList.append(sensor)
                print(f"trigerlist:  {sensorList}")
            sensor_list.append(sensorList)
    return(sensor_list)

