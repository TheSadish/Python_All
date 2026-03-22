# ----------------------------------
# Generator Function
# ----------------------------------

nums = [10,25,35,1,26,29]

print(len([i for i in nums if i > 25]))

# A generator produces values lazily, one at a time, instead of storing them in memory.

x = (i*i for i in range(3))
print(list(x)) # [0,1,4]
print(list(x)) # []

# Generators can be iterated only once because they yield values lazily.