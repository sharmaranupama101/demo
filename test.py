# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import os
# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/v1/docker', methods = ['GET', 'POST'])
def home():
	if(request.method == 'GET'):

		data = "hello docker"
		return jsonify({'data': data})
@app.route('/', methods = ['GET', 'POST'])
def demo():
	if(request.method == 'GET'):

		data = "hello demo first page"
		return jsonify({'data': data})

# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route('/v1/home', methods = ['GET'])
def disp():
  
	data = "hello home"
	return jsonify({'data': data})

# driver function
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
