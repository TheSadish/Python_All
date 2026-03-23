# Two Sum Problem nums = [2, 7, 11, 15] target = 9 Output: [0, 1]

def two_sums(nums,target):
    two_sum_list = []
    for i in range(0,len(nums)-1):
        for j in range(1,len(nums)-1):
            if nums[i]+nums[j]==target:
                two_sum_list.append(i)
                two_sum_list.append(j)
    print(two_sum_list)

nums = [2, 7, 11, 15]
target = 9

two_sums(nums,target)

# Using dictionary

data = dict.fromkeys(nums)
print(data)