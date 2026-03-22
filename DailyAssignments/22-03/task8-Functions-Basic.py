'''
Task 3: Functions 
1. Write function is_even(n) -> returns True/False 
2. Write function sum_list(nums) 
3. Write function to find max of 3 numbers
'''

def is_even(n):
    return (True if n%2==0 else False)

def sum_list(nums):
    return sum(nums)

def max_of_3(a,b,c):
    return max(a,b,c)


print(is_even(3))
print(sum_list([10,20]))
print(max_of_3(1,2,6))