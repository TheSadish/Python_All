'''
List Basics Given: nums = [1, 2, 3, 4, 5, 6] 
1. Reverse the list (without slicing) 
2. Find second largest number 
3. Remove duplicates (preserve order)
'''

nums = [1, 2, 3, 4, 5, 6]
num_reverse = [nums[i] for i in range(len(nums)-1,-1,-1)]

print(num_reverse)

# ---------------------------------------------------------------------

sorted_nums = nums[:]

sorted_nums.sort()
print(sorted_nums[len(nums)-2])

# ---------------------------------------------------------------------

nums1 = [3,4,4,4,5,6,7]

no_dup_num1 = dict.fromkeys(nums1)
print(list(no_dup_num1))