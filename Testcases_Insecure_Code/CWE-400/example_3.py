# Insecure code with uncontrolled resource consumption (disk space)
class LogWriter:
    def __init__(self):
        self.file = open("robot.log", "a")

    def write_log(self, message):
        while True:
            self.file.write(message)

logger = LogWriter()
logger.write_log("Critical operation\n")