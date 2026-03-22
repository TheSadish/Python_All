'''
Task 2: String Logic 
1. Count frequency of characters Input: “aabbccaa”
Output: a: 4 b: 2 c: 2
2.  Remove duplicates Input: “programming” Output: “progamin”
'''

input = "aabbcca"
frequency = {}

for ch in input:
    if ch in frequency:
        frequency[ch]+=1
    else:
        frequency[ch]=1

print(frequency)

# -----------------------------------------------

# Input: “programming” Output: “progamin”
input = "programming"
output = []

for ch in input:
    if ch not in output:
        output.append(ch)
    else:
        continue

output_str = "".join(output)
print(f" Output: {output_str}")
