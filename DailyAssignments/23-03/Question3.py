# Find Missing Number nums: [1, 2, 4, 5] in a series of n positive integers 
# Output: 3

nums = [2, 3, 4, 5]

max_num = max(nums)
probable_sum = max_num*(max_num + 1) // 2   # / 2 - will give float, // 2 will give integer
sum_nums = sum(nums)

print(f"Missing number = {int(probable_sum-sum_nums)}")
