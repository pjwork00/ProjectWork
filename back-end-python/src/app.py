from flask import Flask, render_template, make_response, request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
import os
import time

app = Flask(__name__)

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

#@app.route('/')
#def index(): 
#    context = { 'server_time': format_server_time() }
#    return render_template('index.html', context=context)


@app.route("/", methods=['GET'])
def test():

    # request.method == 'GET'
    return jsonify({'basicElement': 'String returned by python API'})

#@app.route("/<string:key>/", methods=['GET'])
#def notes_list(key):
#request.method == 'GET'
#return key




@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=int(os.environ.get('PORT', 8080)))