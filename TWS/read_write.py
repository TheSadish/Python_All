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

def read_logs():
    file = open("app.logs","r")
    print(file.readlines())
    file.close()

# Using with statement you can avoid closing the file manually
# Rest will be same as read_logs function

def read_logs_with():
    with open("app.logs","r") as file:
        return file.readlines()