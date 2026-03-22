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


'''
In dictionary we can use this to replace the code

if ch in data:
    data[ch] += 1
else:
    data[ch] = 1


data[ch] = data.get(ch, 0) + 1

Here .get will fetch the ch from dictionary and 0 is the default in case there is no value
'''

# A standard Python dictionary retains the insertion order of its items. This behavior was introduced as an implementation detail in Python 3.6 and became an official, guaranteed part of the language specification in Python 3.7 and later.