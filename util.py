import json
import pickle
import os
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower()) #getting the index of location in lower case
    except:
        loc_index = -1 #if location is not present
    
    x = np.zeros(len(__data_columns)) #creating an array of zeros
    x[0] = sqft #taking the input values
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0: #if location is present
        x[loc_index] = 1 #putting the value of location as 1
        
    return round(__model.predict([x])[0],2) #predicting the price

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model
    
    columns_path = r"C:\Users\ACER\Desktop\Mindrisers_Assignment\HousePrice\server\artifacts\columns.json"
    pickle_path = r"C:\Users\ACER\Desktop\Mindrisers_Assignment\HousePrice\server\artifacts\HousesData.pickle"
    
    # Check if files exist
    if not os.path.exists(columns_path):
        print(f"Error: {columns_path} not found")
        return
    
    if not os.path.exists(pickle_path):
        print(f"Error: {pickle_path} not found")
        return
    
    # Load columns.json
    try:
        with open(columns_path, "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file")
        return

    # Load HousesData.pickle
    try:
        global __model
        with open(pickle_path, "rb") as f:
            __model = pickle.load(f)
    except Exception as e:
        print(f"Error: Failed to load pickle file - {e}")
        return

    print("loading saved artifacts...done")

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2)) # other location
