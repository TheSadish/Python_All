import pdb
def read_logs_with():
    with open("app.logs","r") as file:
        return file.readlines()

def analyse(lines):
    # pdb.set_trace() - Used to set a breakpoint for debugging where we can inspect variables and step through the code.(n for next, c for continue, q for quit)
    log_count = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0,
    }
    for line in lines:
        if "INFO" in line:
            log_count.update({"INFO":log_count["INFO"]+1})  # .update() expects a dictionary
        elif "WARNING" in line:
            log_count.update({"WARNING":log_count["WARNING"]+1})
        elif "ERROR" in line:
            log_count.update({"ERROR":log_count["ERROR"]+1})
        else:
            pass

    return log_count
        

lines = read_logs_with()
print(analyse(lines))

