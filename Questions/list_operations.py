mylist = []
input_list =[]

n = int(input())
while (n):
    input_list =  input().split(" ")
    if "insert" in input_list:
        mylist.insert(int(input_list[1]),int(input_list[2]))
    elif "append" in input_list:
        mylist.append(int(input_list[1]))
    elif "pop" in input_list:
        mylist.pop()
    elif "remove" in input_list:
        mylist.remove(int(input_list[1]))
    elif "sort" in input_list:
        mylist.sort()
    elif "reverse" in input_list:
        mylist.reverse()
    elif "print" in input_list:
        print (mylist)
    n -= 1

