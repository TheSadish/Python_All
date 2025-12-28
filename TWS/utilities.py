import json
import requests
import os

def read_logs_with(filename):
    with open(filename,"r") as file:
        return file.readlines()
    
def add_to_json(output_file, json_object):
    with open(output_file, "w") as json_file:
        json.dump(json_object, json_file)