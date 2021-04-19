from flask import Flask, render_template, make_response, request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
import os
import time
from Main_path import Itinerary_creation, test22

app = Flask(__name__)

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)



@app.route("/", methods=['GET'])
def test1():

    # request.method == 'GET'
    return jsonify({'basicElement': 'String returned by python API'})


@app.route("/itinerary", methods=['GET'])
def test():
  selectedBook = request.args.get('selectedBook')
  startDate = request.args.get('startDate')
  endDate = request.args.get('endDate')
  culture = request.args.get('culture')
  nature = request.args.get('nature')
  recreation = request.args.get('recreation')
  speed = request.args.get('speed')
  budget = request.args.get('budget')
  Itinerary=Itinerary_creation(selectedBook, startDate, endDate, culture, nature, recreation, speed, budget)
  #out=test22( culture, nature, recreation, speed, budget)
  # print(out)
  print(str(selectedBook))
  print(str(startDate))
  print(str(endDate))
  print("Culture score: " + culture)
  print("Nature score: " + nature)
  print("Recreation score: " + recreation)
  print("Speed of travelling: " + speed)
  print("Budget available: " + budget)
  # request.method == 'GET'
  result = {
        "output": Itinerary
    }
  result = {str(key): value for key, value in result.items()}
  #return jsonify({'basicElement': 'String returned by python API'})
  return jsonify(result=result)






@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

if __name__ == '__main__':
    app.run(debug=False,host='127.0.0.1',port=int(os.environ.get('PORT', 8081)))