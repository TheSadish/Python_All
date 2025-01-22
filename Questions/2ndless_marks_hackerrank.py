"""
We need to take input as name and marks for more than 2 kids then store them as a list inside a list (Nested list)
Then printout the second lowest marks, in case the marks are same print both of them and in alphabetic order.

[['Sadish',30.0],['Sid',40.0],['Sau',40]]

Output -
Sau
Sid

"""


names = []
n =  int(input())

while (n):
    new_list = []
    new_list.append(input())
    new_list.append(float(input()))
    names.append(new_list)
    new_list = []
    n-=1
    
new_list = []
for i in names:
    new_list.append(i[1])

new_list = list(set(new_list))
new_list.sort()
print(new_list)

if len(new_list) > 1:
    min2 = new_list[1]
else:
    exit
print(min2)
new_str = []

for i in names:
    if i[1]==min2:
        new_str.append(i[0])

new_str.sort()

for i in new_str:
    print(i)




