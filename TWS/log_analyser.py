def read_logs():
    file = open("app.logs","r")
    print(file.readlines())
    file.close()

# Using with statement you can avoid closing the file manually
# Rest will be same as read_logs function

def read_logs_with():
    with open("app.logs","r") as file:
        return file.readlines()

def analyse(lines):
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO":log_count["INFO"]+1})
        elif "WARNING" in line:
            log_count.update({"WARNING":log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR":log_count["ERROR"]+1})
        else:
            pass

    return log_count
        

lines = read_logs_with()
print(analyse(lines))

