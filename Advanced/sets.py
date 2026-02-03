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


# Set Union Operation

num_english = int(input())
english = set(map(int,input().split()))

num_french = int(input())
french = set(map(int,input().split()))

print (len(english | french))


# Pop Remove Discard

n = int(input())
s = set(map(int, input().split()))

num = int(input())

for i in range(num):
    next = input()
    if 'pop' in next:
        s.pop()
    elif 'remove' in next:
        s.remove(int(next.split()[1]))
    elif 'discard' in next:
        s.discard(int(next.split()[1]))

# print(sum(s))
