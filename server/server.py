from flask import Flask, request, jsonify
import util  # Import utility functions

app = Flask(__name__)

# Route to get location names
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # CORS

    return response

# Route to predict home price
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # Retrieve form data and convert to appropriate types
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Call utility function to get price estimate
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')  # CORS

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Load model and columns data
    app.run()
