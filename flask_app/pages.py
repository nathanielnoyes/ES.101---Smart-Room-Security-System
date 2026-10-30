from flask import Flask, jsonify, request, render_template
import json
import datetime
import sqlite3#tables are sensors and triggers
database = "database.db"

def events(table):
    
    event = render_template("events.html", table = table)
    with sqlite3.connect(database) as connect:
        cursor = connect.cursor()
        triggers = cursor.execute(f"select * from {table};")
        trigger_list = []

        for trigger_subList in triggers:
            triggerList = []
            for trigger in trigger_subList:
                triggerList.append(trigger)
                print(f"trigerlist:  {triggerList}")
            trigger_list.append(triggerList)
    return(event)