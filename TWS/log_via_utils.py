import pdb
from utilities import *
'''
Packages: These are external libraries or modules that provide additional functionality to your code. 
Python functions that can we called in some other file.
'''

def analyse(lines):
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO":log_count["INFO"]+1})  # .update() expects a dictionary
        elif "WARNING" in line:
            log_count.update({"WARNING":log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR":log_count["ERROR"]+1})
        else:
            pass

    return log_count
        

add_to_json("output.json",analyse(read_logs_with("app.logs")))