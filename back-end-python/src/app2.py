from flask import Flask, render_template, make_response, request, url_for, jsonify
from flask_api import FlaskAPI, status, exceptions
import os
import time
import Analysis_data
app = Flask(__name__)

def format_server_time():
  server_time = time.localtime()
  return time.strftime("%I:%M:%S %p", server_time)

def do_something(text1,text2):
   text1 = text1.upper()
   text2 = text2.upper()
   combine = text1 + text2
   return combine


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    word = request.args.get('text1')
    text2 = request.form['text2']
    combine = do_something(text1,text2)
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)


# @app.route("/", methods=['GET'])
# def test():

#     # request.method == 'GET'
#     return jsonify({'basicElement': 'String returned by python API'})
#     #return Analysis_data.prova_1()



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