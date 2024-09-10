'''Implement a Robot class with proper locking mechanism for updating command history in a multi-threaded environment.'''
# Secure code with thread-safe command execution
class Robot:
    def __init__(self):
        self.command_history = []
        self.lock = threading.Lock()

    def execute_command(self, command):
        with self.lock:
            self.command_history.append(command)

robot = Robot()
threading.Thread(target=robot.execute_command, args=("move forward",)).start()
threading.Thread(target=robot.execute_command, args=("turn left",)).start()