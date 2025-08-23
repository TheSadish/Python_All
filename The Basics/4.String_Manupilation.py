str1 = "Sadish"
str2 = "Dash"

concat = str1 + " " + str2 # Sadish Dash
length = len(str1) # 6

# Lower and upper
lower = str1.lower() # sadish
upper = str1.upper() # SADISH

# Replace -> Replace a substring with another substring
name = "Sadish Dash"
name1 = name.replace("Dash","Kumar") # Sadish Kumar

# Split -> Split a string into a list
split = name.split() # ['Sadish','Dash'] -> Splited via space
split = name.split("a") # ['S', 'dish D', 'sh'] -> Splited via 'a'
split = name.split("a", 1) # ['S', 'dish Dash'] -> Splited via 'a' only once since we specified maxsplit = 1

# Strip -> Remove whitespace
text = "  Hi my name is Sadish  "
text = text.strip() # 'Hi my name is Sadish'
text = text.lstrip() # 'Hi my name is Sadish'
text = text.rstrip() # '  Hi my name is Sadish'

#Slice -> Extract a portion of a string
text = "Hi my name is Sadish"
slice = text[0:5] # 'Hi my'
slice = text[-3:] # 'ish' -> -3 means start from the 3rd last character to the end

# Substring -> Part of a string
text = "Hi my name is Sadish"
substring = "is"

if substring in text:
    print("Substring found") 

# Join -> Join a list of strings into a single string
list = ["Hey", "there", "I", "am", "Sadish"]
join_str = " ".join(list) # Hey there I am Sadish -> Joined via space


# Find -> Finds a particular substring

text = "Hey you, how are you ?"
found = text.find("you",5,20) # 4 -> Returns the starting index of the string provided
print(found)

'''
indices = [i for i in range(len(text)) if text.startswith("you", i)]
print(indices)  # Output: [4, 13]

indices = []
for i in range(len(text)):
    if text.startswith("you",i):
        indices.append(i)
print(indices)
'''

# Replace -> Replaces a substring

text = "Hey you, how are you ?"
text = text.replace("you", "they")

# Check content

text = "Kemcho Sadish"
text1 = "Hello123"

text.isalpha()    # False -> Because of space
text1.isalnum()   # True -> Because it contains letters and numbers
text1.isalpha()    # False -> Because of numbers