
from flask import Flask, request, jsonify, render_template # flask is a module that allows you to write python service which can serve http requests
app = Flask(__name__) # create an instance of the Flask class
import util
import os


app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'HousePrice', 'templates'))

@app.route("/")
def home():
    return render_template("app.html")

@app.route("/get_location_names") # route() decorator is used to bind a function to a URL
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/predict_home_price", methods=['POST']) # methods=['POST'] is used to specify the type of request the route should accept
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    bath = int(request.form['bath'])
    bhk = int(request.form['bhk'])
    location = request.form['location']
    
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For House Price Prediction...")
    util.load_saved_artifacts()
    app.run()
