file = open("The Basics/TWS.py", "r+")
print(file.read())
file.write('\n# File handling in Python\n')
# file.write('\nprint("File handling in Python")\n')
file.close()

# Modes to open a file
# r - read
# r+ - read and write
# w - write (overwrites the file)
# w+ - write and read
# a - append
# a+ - append and read

