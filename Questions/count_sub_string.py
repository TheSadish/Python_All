def count_substring(string, sub_string):
    start = 0
    strCount = 0
    while True:
        start = string.find(sub_string, start)
        if start == -1:
            break
        strCount += 1
        start += 1
    return strCount

string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)