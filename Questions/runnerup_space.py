# Enter your code here. Read input from STDIN. Print output to STDOUT

str = input()
n = int(str.split(" ")[0])
m = int(str.split(" ")[1])

list_n = []
list_A = []
list_B = []


str = input()

list_n = str.split(" ")

# print(list_n)


str = input()
list_A = str.split(" ")
# print(list_A)

str = input()
i=0

list_B = str.split(" ")

# print(list_B)

print(len(list(set(list_n).intersection(list_A)))-len(set(list_n).intersection(list_B)))



