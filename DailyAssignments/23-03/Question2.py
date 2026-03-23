# Move Zeros Input: [0, 1, 0, 3, 12] Output: [1, 3, 12, 0, 0]

nums = [1, 0, 0, 3, 12]

count=[]
for i in range(0,len(nums)-1):
    if nums[i] == 0:
        count.append(i)
    


print(nums)
