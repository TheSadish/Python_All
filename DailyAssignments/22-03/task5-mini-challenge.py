'''
Input nums = [1, 2, 3, 4, 5, 6]
Output:
Even sum = 12
Odd sum = 9
'''

nums = [1, 2, 3, 4, 5, 6]

even_sum = sum(i for i in nums if i%2==0)
odd_sum = sum(i for i in nums if i%2!=0)

print(f"Even Sum = {even_sum} \nOdd Sum = {odd_sum}")

# -----------------------------------------------------

'''
Real Problem Input: “hello world” Output: h:1 e:1 l:3 o:2 w:1
r:1 d:1 (ignore spaces)
'''

input = "hello world"
data = {}

for ch in input:
    if ch == " ":
        continue
    elif ch in data:
        data.update({ch: data[ch]+1})
    else:
        data[ch]=1

print(data)


# -------------------------------------------------

# Mini Challenge Input: “madam” Output: “Palindrome”

input = "madam"

palindrome = ("Palindrome" if input==input[::-1] else "Not a palindrome")
print(f"Output: {palindrome}")
