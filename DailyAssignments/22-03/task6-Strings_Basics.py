'''
Reverse the string
Convert to uppercase
Count number of vowels 
Check if string is palindrome
'''

text = "python"

reverse = text[::-1]
print(reverse)
print(text.upper())

vowels = sum(1 for ch in text if ch in ['a','e','i','o','u'])
print(f"Number of vowels are {vowels}")

if text==reverse:
    print("Text is palindrome")
else:
    print("Not Palindrome")