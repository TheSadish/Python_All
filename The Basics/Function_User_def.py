# Basic Calculator with + - * /

def add(a,b):
    return a+b

def sub(a,b):
    return abs(a-b)

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

symbol = int(input("What operation you want to perform ? 1. Add 2. Sub 3. Multi 4. Division  - > "))

if(symbol == 1):
    print(f"The sum of these 2 numbers is {add(a,b)}")
elif symbol == 2:
    print(f"The diff of these 2 numbers is {sub(a,b)}")
elif symbol == 3:
    print(f"The multi of these 2 numbers is {mul(a,b)}")
elif symbol == 4:
    print(f"The division of these 2 numbers is {div(a,b)}")
else:
    print("Enter a valid input")


# Add all digits in a list
    
def addition(arg):
    sum=0
    for i in arg:
        sum+=i
    return sum

tobeadded = []

n = int(input("Enter the number of digits you want to add : "))
print("Enter the numbers : ")
while (n):
    a = int(input())
    tobeadded.append(a)
    n-=1

print (f"The digits provided by you are {tobeadded} and the sum is {addition(tobeadded)}")
