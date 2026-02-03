# Enter your code here. Read input from STDIN. Print output to STDOUT

# myList = ['1','2','3','4']
set1 = set()
set2 = set()
    
m=int(input())
set1 = set(map(int,input().split()))

n=int(input())
set2 = set(map(int,input().split()))


mylist = list(map(int,set2.symmetric_difference(set1)))
mylist.sort()

# print(f'{type(mylist)} and value is {mylist}')
for i in range(0, len(mylist)):
    print(mylist[i])
    
    
# print(permutations)