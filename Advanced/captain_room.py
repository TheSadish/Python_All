# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k=int(input())
entry_list = list(map(int, input().split()))

counter_list = Counter(entry_list)

# print(counter_list) Output will be like Counter({1: 2, 2: 2, 3: 1, 4: 1, 5: 1}) of type counter
# Counter_list.items()
for key,items in counter_list.items():
    if items == 1:
        print(key)
        break

# Counter - Counts the occurrences of each element in the list

# Here counter_list.item() will be a dictionary where key is the element and value is the count of occurrences

# Note : looping over dictionary will only give the keys, to get the values we need to
# use .items() method which will return a list of tuples where each tuple is (key, value) pair. 
# sWe can unpack the tuple in the for loop to get key and value separately.