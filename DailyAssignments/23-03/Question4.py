'''
Input : [1, 2, 3, 4, 5] 
k = 2

Output = [4, 5, 1, 2, 3]
Rotate list by k steps

'''

nums = [1, 2, 3, 4, 5] 
k=2
length = len(nums)

if k > length:
    k= k % length

duplicate = nums[:]

for i in range(length):
    j=(i+k)%length
    duplicate[j]=nums[i]

print(duplicate)