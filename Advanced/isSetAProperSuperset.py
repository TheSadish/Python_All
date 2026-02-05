# # Enter your code here. Read input from STDIN. Print output to STDOUT

setA = set(map(int,input().split()))

n = int(input())
counter = True

if (n > 21) or (len(setA) > 501):
    print(False)
    exit()

for i in range(0,n):
    setB = set(map(int,input().split()))
    # if (len(setB)>=len(setA)):
    #     counter=0
    # elif (len(setA.intersection(setB))<len(setA)):
    #     counter=1
    counter = counter and setA.issuperset(setB) and len(setA)>len(setB)
    # if (setA.issuperset(setB)) and (len(setA) > len(setB)) and (counter is True):
    #     counter = True
    # else:
    #     counter = False
    
print(counter)
 
