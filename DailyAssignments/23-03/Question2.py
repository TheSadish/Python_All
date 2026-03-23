# Move Zeros Input: [0, 1, 0, 3, 12] Output: [1, 3, 12, 0, 0]

nums = [0, 1, 0, 3, 12]

new_list, count = [],0

for i, num in enumerate(nums):
    if num != 0:
        new_list.append(num)
    else:
        count+=1

for i in range(count):
    new_list.append(0)

# print(new_list)

#--------------------------------------------------------------------
# Using single list only (in-place solution)

index = 0

for i,num in enumerate(nums):
    if num != 0:
        nums[index]=num
        index += 1
    
for i in range(index, len(nums)):
    nums[index] = 0
    index += 1

print(nums)