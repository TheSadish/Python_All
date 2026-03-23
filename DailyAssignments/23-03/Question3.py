# Find Missing Number Input: [1, 2, 4, 5] Output: 3

Input = [1, 2, 4, 5]

max_num = max(Input)
probable_sum = max_num*(max_num + 1)/2
sum_input = sum(Input)

print(f"Missing number = {int(probable_sum-sum_input)}")
