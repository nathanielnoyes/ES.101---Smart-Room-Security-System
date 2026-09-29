from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/data', methods=['POST'])
def receive_data():
    # Get JSON data sent from the Feather HUZZAH
    data = request.json
    print("Received data from Feather:", data)
    return jsonify({"status": "success", "received": data}), 200

if __name__ == '__main__':
    # Run on 0.0.0.0 so it is accessible on your local network
    app.run(host='0.0.0.0', port=5000, debug=True)
