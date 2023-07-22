# 
# Name : Yigit Hakverdi
# Date : 07.08.2023
# Description : Feature extraction from the regulations it is a generic script that
#               can be used for any regulation.
# 

import json

# Path of the regulations data, careful with the JSON structure, as defined on the 
# description and in the given example regulations.json
path = "./../data/regulations.json"

# Read the data from the JSON file returns the dictionary object. Once the JSON is correctly 
# structured, following examples show how to access certain data in the. Python dictionary object 
# print(read_data()["data"][0]["regulations"][0]["value"])
def read_data():    
    with open(path) as f:
        data = json.loads(f.read())
        return data

def read_text():
    pass

def get_features():
    pass

