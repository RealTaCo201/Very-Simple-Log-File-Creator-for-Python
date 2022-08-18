import datetime

class Logger:

    # Initialization
    def __init__(self, output_folder):
        self.output = output_folder
        if self.output[len(self.output) - 1] != "/" or self.output[len.self.output - 1] != "\\":
            self.output += "/"

    # Writing to log file
    def log(self, data):
        current_date = datetime.datetime.now()
        log_file_name = str("log " + str(current_date.month) + "-" + str(current_date.day) + "-" +
                            str(current_date.year) + ".txt")
        log_txt = open(self.output + log_file_name, "a+")
        current_time = datetime.datetime.now()
        log_txt.write(str(current_time.month) + "-" + str(current_time.day) + "-" + str(current_time.year)[2:4]
                    + "@" + str(current_time.hour) + ":" + str(current_time.minute) + ":" + str(current_time.second)
                    + ":  " + data + "\n")
        log_txt.close()
