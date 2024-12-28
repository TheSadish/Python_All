"""
Variable Length Argument **    kwargs (Keyword Argument -> Dictionary)
Write a function to take some minutes and some key values like hobby, work then throw a random min for random hobby
"""
import random

def activity(*args,**kwargs):
    min = sum(args) + random.randint(0,60)
    choice =  random.choice(list(kwargs.keys()))
    print(f"You can spend {min} min in {kwargs[choice]}")    
       

activity(10,20,30,hobby="Sing",work="Azure",fun="Games")
