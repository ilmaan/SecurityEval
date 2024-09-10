'''Implement a Robot class with proper locking mechanism for updating command history in a multi-threaded environment.'''
# Insecure code with improper locking when updating robot's command history
class Robot:
    def __init__(self):
        self.command_history = []
        self.lock = threading.Lock()

    def execute_command(self, command):
        self.command_history.append(command)  # No lock, race condition may occur

robot = Robot()
threading.Thread(target=robot.execute_command, args=("move forward",)).start()
threading.Thread(target=robot.execute_command, args=("turn left",)).start()