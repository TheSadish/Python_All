

"""
print("Hello World") 

num = {int(input("Write a number: "))}
print(f"The input number was {num} \n") 

# Type casting - Conversion of one data type to another data type.

env = input("Enter the environment: ")
print(f"The environment is {env}")  

if (env == "Prod"):
    print("You are in Production Environment")
elif (env == "QA"):
    print("You are in QA Environment")
else:
    print("You are in Dev Environment") 

# Identation is very important in Python.

# LOOPS

# FOR LOOP 
# # Range works like this: range(start, end-1, increment/decrement)

list= []

for i in range(1,6):
    list.append(int(input(f"Enter number {i} :")))

print(list)

# WHILE LOOP

num1 = 2
while num1 != 0:
    num1 = int(input("Enter a number (0 to exit): "))
    print(f"You entered: {num1}")


# Functions

def kaam(env): # Function Definition
    if env == "Prod":
        print("Dont deploy on Friday")
    elif env == "QA":
        print("Test cases should pass")
    else:
        print("Deploy anytime")

env = input("Enter your env :")
kaam(env) # Function calling



# Check Cif CPU Usage > Threshold
import psutil # type: ignore

def get_cpu_threshold():
    threshold = int(input("Enter CPU threshold in % "))
    check_cpu(threshold)

def check_cpu(thres):
    cpu_usage = int(psutil.cpu_percent(interval=1)) # Need to import psutil module and you need to install through pip
    print(f"Your current CPU Usage is {cpu_usage} \n")
    if cpu_usage > thres:
        print("CPU Usage exceeded. Email SENT! ")
    else:
        print("CPU is in safe state.")

get_cpu_threshold()


# Data Structure - List, Dicitionary, Set, Tuple

# List

clouds = ["Azure","AWS","GCP","Alibaba"]

clouds.append("Oracle")

print(clouds)
print(len(clouds))
print(clouds[0])
print(clouds[-1])

# print(dir(clouds))
print(clouds.extend.__doc__)

for cloud in clouds:
    print(cloud)


# Dictionary

my_dict = {
    "name":"Sadish",
    "age":26
    }

print(f"My name is {my_dict['name']}")
print(f"My name is {my_dict.get("aghe")}") # .get() wont throw an error if the argument isnt found

my_dict.update({"LastName":"Dash"})
print(my_dict)

print(my_dict.items()) # This returns a list of tuples which contains key value pairs

for i in my_dict:
    print(i) # This will print only keys as default behavior of dictionary is to iterate over keys

for key,value in my_dict.items():
    print(f"{key} = {value}") 

# Set - Unordered collection of unique items

info = {} # Empty Dictionary
days = set() # Empty Set
dic = dict() # Another way to declare empty dictionary

days = {2,3,4,3,2,2,2,3,4,5,3,2,1,2,3,4,5}
print(days) # Set will remove duplicates

# Does set sorts itself? No, sets are unordered collections. 
# It can change order every python version.
# To make it sorted use sorted() function

num = [0,9,8,9,0,1,2,-1,2,3,4,5,3,2,1,0,-1]

num = list(set(num))
print(num)



# Tuple - Immutable (Cannot be changed)

tuple1 = (1,2,3,4,5)
print(tuple1)

print(tuple1.count(2)) # Counts how many times 2 is present in the tuple
print(tuple1.index(4)) # Returns the index of the value 4
for i in tuple1:
    print(i)

# You cannot add, remove or update values in a tuple


#apparent_encoding', 'close', 'connection', 'content', 'cookies', 'elapsed', 'encoding', 
# 'headers', 'history', 'is_permanent_redirect', 'is_redirect', 'iter_content', 'iter_lines', 'json', 
# 'links', 'next', 'ok', 'raise_for_status', 'raw', 'reason', 'request', 'status_code', 'text', 'url


# Simple API call using requests module

import requests # type: ignore

url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(url)

for key,value in response.json().items():
    print(f"{key} = {value}")



import requests # type: ignore


PAT_KEY = "demo"

url = 'https://www.alphavantage.co/'

interval = "5min"
symbol = input("Enter the stock symbol (Type IBM): ")
query = f"query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={PAT_KEY}"

def get_market_date(url, query):
    response = requests.get(url+query)
    print(response.json()['Meta Data']['3. Last Refreshed'])

get_market_date(url, query)

"""
import requests # type: ignore

url = "https://official-joke-api.appspot.com/random_joke"

def get_joke():
    response = requests.get(url)
    return (response.json()['setup']+ "\n" + response.json()['punchline'])

print(get_joke())