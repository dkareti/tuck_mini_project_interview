# This file will contain all the endpoints to manage the data
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

#define routes
@app.route("/getinfo", methods=[])

if __name__ == '__main__':
    #run the app on port 3001
    app.run(host='0.0.0.0', port=3001, debug=True)