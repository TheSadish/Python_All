''' 
Fetch data from STRING
               a = E  a  r  t  h
               1  2  3  4  5
              -5 -4 -3 -2 -1  
'''
planet = "EarthMarsJupiter"
print(planet) 
#print(planet[4], planet[6], planet[-18])

print(planet[0:5])   # Slicing from index 0 to 4 (inclusive of 0, exclusive of 5 that is till 4)
print(planet[:])     # By default range is 0:-1  (Start to End)



# Fetching Data from Tuple / Same works for List as well 

myself = ("Sadish", 25, "Accenture")
print(myself[1:3])   # Same way like string
print(myself[-1]) # Fetching last element

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


a = "Sadish"
b = "Kumar"
c = "Dash"

print(a+ " " +b+ " " +str(6+6) + " " +c)  #Contatenation of strings

# Spliting a string

a = "Sadish Kumar Dash"

print(a.split(" ")) # Prints a list of words in the string

print(a.split(" ")[0]) # Prints the first word in the string
