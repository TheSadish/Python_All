# First non-repeating character

text = "aabbcdeff"
data = {}

for ch in text:
    data[ch] = data.get(ch, 0) + 1

non_repeat = False

for key,value in data.items():
    if value==1:
        print(f"Non repeating character is {key}")
        non_repeat = True
        break

if not non_repeat:
    print("There are no non-repeating characters")


# print(data)