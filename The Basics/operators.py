# Arithmetic Operators

x = 2
y = 5
total = x+y
print(total)

total = y-x
print(total)

total = y*x
print(total)

total = y/x
print(total)


total = y%x
print(total)

total = y**x
print(total)

# Comparisions Operators

a = 30
b = 60

out = a < b
print(out)

'''
Others are > <= >= != ==
'''

# Assignment Operator

c = 0
d = 1

c+=d  # c=c+d
print(c)

# Logical Operators - and/or

a = 40
b = 60
x = 2
y = 3

if (a/x == 0 or b%y == 0):
    print("Statement is True")
else:
    print("False")

out = not[(a < b) or (x < y)]  # not - negates the output
print(out)


# Membership Operators  in/not in- basically checks if a string/int exists in a tuple/list of dictionary

myself = {
    "name":"Sadish",
    "age":25,
    "Company":"Accenture",
    "Certs":["900","104","400","204"]
}

myself_tuple = ("Sadish", 25, "Accenture")

print("name" in myself)
print(251 not in myself_tuple)


str = "Sadish"        
print("Sad" in str)     # Works in string as well

# Identity Operators - is/is not (just like comparision operator)

a = 12
b = 13

print(a is b)

