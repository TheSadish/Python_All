# Variable assignments

var1 = "Sadish" # Other ways of string - var1 = 'Sadish', var1 = '''Sadish'''
var2 = 25
var3 = 15.5

print (var1)
print (var2)
print (var3)
print ()
a = b = c = 65

print (b)

x, y, z, w = "alpha", "beta", 12, 5.4

print ("Variable x value is", x, "of type", type(x))
print ("Variable w value is", w)
print ()

# Get the data type
print (type(w))
print (type(x))
print (type(y))

str1 = "Dash"

# List / Collection of variables - Enclosed in square brackets  - Mutable / Editable

first_list = [str1, "Python", 2.45, 3, "Mama"]
print (first_list)

first_list[1] = "Not"  # List editing is possible
print (first_list)

# Tupple / Collection of variables - Enclosed in round brackets - Immutable / Non -Editable

first_tuple = (str1, "Python", 2.45, 3, "Mama")
print (first_tuple)

# first_tuple[1] = "Not" # Tuple editing is not possible

# Dictionary - Key Value Pairs - Curly brace

first_dict = {
    "Name":"Sadish",
    "Age":25,
    "Skills":["Python", "Azure", "Linux"]
}

print (first_dict)

# Boolean

x = True
y = False

if x == True:
    print ("Yes")
