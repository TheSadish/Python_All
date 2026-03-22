# Input
# nums = [1, 2, 3, 4, 5, 6]

# Output:

# Even sum = 12
# Odd sum = 9

nums = [1, 2, 3, 4, 5, 6]

even_sum = sum(i for i in nums if i%2==0)
odd_sum = sum(i for i in nums if i%2!=0)

print(f"Even Sum = {even_sum} \nOdd Sum = {odd_sum}")