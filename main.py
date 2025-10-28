# This file will contain all the endpoints to manage the data
from flask import Flask, request, render_template, jsonify
from functions import access_field, modify_json, read_json
app = Flask(__name__)

#import the json output from the custom GPT
JSON_FILE = './dev/test.json'

#global data
data = access_field()

#define routes
@app.route("/getinfo", methods=['GET'])
def get_info():
    '''
    This function prints out the contents of 'gptOutput'.
    '''

    return data

@app.route("/modify", methods=['POST'])
def modify_info(new_string: str):
    '''
    This function updates the global 'getOutput' data.
    '''
    global data

    json_info = read_json()

    data = modify_json(JSON_FILE, new_string, json_obj=json_info)


if __name__ == '__main__':
    #run the app on port 3001
    app.run(host='0.0.0.0', port=3001, debug=True)