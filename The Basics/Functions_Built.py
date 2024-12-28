# Built In Functions Strings

message = "my name is Sadish Kumar Dash and my age is 25"

print(message.capitalize())   # Make the first character of string as capital
 
print(dir(message))   # Prints all available methods for the given parameter

'''
.upper() - Converts entire message to upper
.lower()  - Converts everything to lower
.islower() -  Returns boolean if all lower

.find("abc") - Find the substring "abc" in the entire string and returns the index value where it starts 
'''

seq1 = ("192","168","49","12")
a = "."
print(a.join(seq1))
print(".".join(seq1))      # a.join(b) - combines a with b. If B is a tuple or list, join combines a with each one of the value


# Functions in a list

names  = ["Sadish","Sidhant","Saurabh"]

names.append("Gaurav") # Insert at then last

names1 = ["Richa","Shefali"]

names.extend(names1)   # Add two list together


names.insert(2, "Sumit") # Insert a specific place

names.pop() # Remove the last element

names.pop(5) # Remove the 5th element

print(names) 

# Functions in a dictionary

first_dict = {
    "Name":"Sadish",
    "Age":25,
    "Skills":["Python", "Azure", "Linux"]
}

print(first_dict.pop("Age"))  # Remove the key you want to remove

print(first_dict.items())


