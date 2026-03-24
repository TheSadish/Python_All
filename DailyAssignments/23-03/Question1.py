# Two Sum Problem nums = [2, 1, 11, 7] target = 9 Output: [0, 1]

def two_sums(nums,target):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]   # O(n^2) - time complexity
            

            
'''
def two_sums_no_j(nums,target):
    for i in range(0,len(nums)):
        needed = target - nums[i]
        if needed in nums & needed!=nums[i]:
            return [i, nums.index(needed)]

print(two_sums_no_j(nums, target))
list can have duplicates so
.index() will only get the index of first found index in case of duplicate numbers
'''

nums = [2, 1, 11, 10, 7]
target = 9

# print(two_sums(nums, target))


# Using dictionary

seen = {}

for i in range(len(nums)):
    need = target - nums[i]
    
    if need in seen:
        print([seen[need],i])
    else:
        seen[nums[i]]=i

# Ulta approach used , not like i=0 pe sara check, fir i=0 pe sara check
# Better ki jo dekha usko save karo and check using that

'''
seen1 = {}

for i, num in enumerate(nums):
    seen1[num]=i

for i in range(len(nums)):
    needed = target - nums[i]

    if needed in seen1:
        print([i,seen1[needed]])
        break

# nums = [2, 1, 11, 10, 7]
seen1 = {2:0,1:1,11:2,10:3,7:4}
# print(seen1)


Here I am using future elements - not good

Index issue might come [3,2,4] can give [3,3]
'''