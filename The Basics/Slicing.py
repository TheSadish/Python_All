''' 
Fetch data from STRING
               a = E  a  r  t  h
               1  2  3  4  5
              -5 -4 -3 -2 -1  
'''
planet = "Earth Mars Jupiter"
print(planet) 
print(planet[4], planet[6], planet[-18])

print(planet[0:5])   # Slicing [first range: Last +1]
print(planet[:])     # By default range is 0:-1  (Start to End)



# Fetching Data from Tuple / Same works for List as well 

myself = ("Sadish", 25, "Accenture")
print(myself[1:3])   # Same way like string
print(myself[-1])

print(myself[1:3][1]) # Slicing a sliced tuple

print(myself[1:3][1][0:4]) # Slicing a string from the outptut of a sliced tuple


# Fetching Data from Dictionary

myself = {
    "name":"Sadish",
    "age":25,
    "Company":"Accenture",
    "Certs":["900","104","400","204"]
}

print (myself["name"][0:4])
print (myself["Certs"][-2][:2])