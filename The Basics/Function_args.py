# # Variable Length Argument (Non keyword Argument)

# def food(first_order, *args):
#     print(f"The first order is {first_order}")
#     # print(type(args))  Here args is a tuple
#     if len(args) > 0:
#         print("Rest orders are")
#         for i in args:
#             print (i)

# print("Enter the rest 3 food items")

# food("Salad",input(),input(),input())

# Variable Length Argument (Non keyword Argument)

def food(first_order, *args):
    print(f"The first order is {first_order}")
    # print(type(args))  Here args is a tuple
    if len(args) > 0:
        print("Rest orders are:")
        for i in args:
            print(i)

print("Enter the rest 3 food items:")

# Collecting user inputs with prompts
rest_orders = [input() for i in range(3)]
print(rest_orders)
# Unpacking the list into the function call
food("Salad", *rest_orders) #This * unpacks the list into individual elements