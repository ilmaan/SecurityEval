'''Implement a Robot class with proper access control for adding log entries.'''
# Insecure code with improper access control (public access to critical logs)
class Robot:
    def __init__(self):
        self.log = []

    def add_log(self, entry):
        self.log.append(entry)

robot = Robot()
robot.add_log("Movement started")  # Public access to logs