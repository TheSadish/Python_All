# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

k=int(input())
entry_list = list(map(int, input().split()))

counter_list = Counter(entry_list)

for key,items in counter_list.items():
    if items == 1:
        print(key)
        break

# Counter - Counts the occurrences of each element in the list

# Here counter_list.item() will be a dictionary where key is the element and value is the count of occurrences