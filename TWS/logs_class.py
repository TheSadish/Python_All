import json
class LogAnalyzer:

    def __init__(self, file_name, output_file):
        self.file_name = file_name
        self.output_file = output_file

    def read_logs_with(self):
        with open("app.logs","r") as file:
            return file.readlines()
        
    def add_to_json(self, counts):
        with open(self.output_file, "w") as json_file:
            json.dump(counts, json_file)

    def analyse(self):
        lines = self.read_logs_with()
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

        self.add_to_json(log_count)
    
logs = LogAnalyzer("app.logs", "output.json")
logs.analyse()