

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

"""

# Check Cif CPU Usage > Threshold
import psutil

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