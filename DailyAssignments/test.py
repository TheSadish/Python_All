'''
Input : [1, 2, 3, 4, 5] 
k = 2

Output = [4, 5, 1, 2, 3]
Rotate list by k steps

'''


text = [1, 2, 3, 4, 5]
k=6

if k > len(text):
    k = k % len(text)

new_list = text[:]

for i, num in enumerate(new_list):
    text[(i+k)%len(text)] = num

print(text)