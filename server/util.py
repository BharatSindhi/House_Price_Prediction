import pickle
import json
import numpy as np

# Declare global variables for location, columns, and model
__locations = None
__data_columns = None
__model = None

# Define the function to get the estimated price based on input features
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1  # If location not found, set to -1

    # Create input array for prediction
    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict and return the price, rounded to 2 decimal places
    return round(__model.predict([x])[0], 2)

# Define the function to load saved artifacts (model and columns)
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __locations

    # Load column names from the JSON file
    with open(r"D:\ML_Project\House_Price_Prediction\server\artifacts\columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # First 3 columns are sqft, bath, bhk

    # Load the saved model from the pickle file
    global __model
    if __model is None:
        with open(r"D:\ML_Project\House_Price_Prediction\server\artifacts\banglore_home_prices_model.pickle", 'rb') as f:
            __model = pickle.load(f)
    print("Loading saved artifacts...done")

# Function to get location names
def get_location_names():
    return __locations

# Function to get all data columns
def get_data_columns():
    return __data_columns

# Test code block for module functionality (optional)
if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2))  # Other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # Other location
