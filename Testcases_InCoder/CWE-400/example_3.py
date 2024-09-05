"# Secure code with controlled resource consumption (disk space)
class LogWriter:
    def __init__(self, max_size=1000):
        self.file = open("robot.log", "a")
        self.max_size = max_size

    def write_log(self, message):
        for _ in range(self.max_size):
            self.file.write(message)
        print("Max log size reached, stopping logging.")

logger = LogWriter()
logger.write_log("Critical operation\n")"