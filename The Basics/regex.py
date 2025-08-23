import re

# Check for the exact word "ERROR" in a string
text = "2025-08-21 ERROR: Disk space low" 

match = re.search("ERROR2", text)   # look for the exact word ERROR
if match:
    print("Found:", match) # .group() gives the matched text
else:
    print(f"Not found {match}") # Now match is None

# Find all digits in a string

line = "Low Disk Space: Error code 404 Date: 2025-08-21"

match = re.findall(r"\d+", line)
if match:
    print("Found match @ ", match)
else:
    print("No match found")

# Check for multiple spaces in a string

line = "User_1  logged in at 10:30 PM on 2025-08-21"

match = re.findall(r"\s{2,}", line)
if match:
    print("Found multiple spaces")

# Character set example

list = "cat, bat, rat, dog, log"
match = re.findall(r"[abc]at", list)
print("Found character set match:", match)

# Match a date in YYYY-MM-DD format using groups

log = "2025-08-21 ERROR Disk failure"
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", log)
print(match.groups())