# Do:

# Print all elements
# Print sum of list
# Find max number
# Count how many numbers are > 25

nums = [10, 20, 30, 40, 50]

for num in nums:
    print(num)

total=0
for num in nums:
    total+=num
print(total)

print(max(nums))

# Count how many numbers are > 25
count = sum(1 for i in nums if i > 25)
print(count)

# Creating a list and then counting the length
print(len([i for i in nums if i > 25]))

# A generator produces values lazily, one at a time, instead of storing them in memory.

x = (i*i for i in range(3))
print(list(x)) # [0,1,4]
print(list(x)) # []

# Generators can be iterated only once because they yield values lazily.