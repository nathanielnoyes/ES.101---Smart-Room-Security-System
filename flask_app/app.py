from flask import Flask, jsonify, request
import json
import datetime
import sqlite3#tables are sensors and triggers

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    print("fish")
    data = request.json
    if data["Button"] == "on":
        return("doit")
    print("Received data from Feather:", data)
    date = datetime.datetime.now()
    command = f"insert into triggers values({},{},{})"
    cursor.execute("")
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    