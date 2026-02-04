# Enter your code here. Read input from STDIN. Print output to STDOUT

test_cases = int(input())

for i in range(0, test_cases):
    set1_len = int(input())
    set1 = set(map(int,input().split()))
    
    set2_len = int(input())
    set2 = set(map(int,input().split()))
    
    if (set1_len > set2_len):
        print(False)
    elif (len(set1.intersection(set2))==set1_len):
        print(True)
    else:
        print(False)
    
