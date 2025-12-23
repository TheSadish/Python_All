import random
import re

dic = {
    "a": 1,
    "b": 2,
    "c": 3
}

rand_key = random.choice(list(dic.keys()))
print(rand_key)
print(dic[rand_key])


# Importing re module
string = "Hello, my name is John, I am 23 years old. My number is 12345"

new_string = re.sub('[A-Za-z,. 1-9]','',string)
print(new_string)