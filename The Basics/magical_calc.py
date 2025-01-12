
def magical_calc():
    global run  # This is a global variable that can be accessed from anywhere in the program
    global previous
    equation = ""
    if previous == "a":
        equation = input("Enter an equation: ")
    else:
        equation =  input(str(previous)) # Uses the value of previous as the prompt
                          
    if equation == "quit":
        print("Quittin")
        run = False
    else:
        if previous == "a":
            previous = eval(equation)
        else:
            previous = eval( str(previous) + equation)
        print(f"Your equation is {previous}")

print("Magic Calculator")
print("Enter 'quit' to exit\n")

run = True
previous = "a"

while run:
    magical_calc()

