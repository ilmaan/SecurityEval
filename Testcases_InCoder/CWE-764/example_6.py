# Secure code using lock to safely update command history
class Robot:
    def __init__(self):
        self.command_history = []
        self.lock = threading.Lock()

    def execute_command(self, command):
        with self.lock:  # Locking to prevent race condition
            self.command_history.append(command)

robot = Robot()
threading.Thread(target=robot.execute_command, args=("move forward",)).start()
threading.Thread(target=robot.execute_command, args=("turn left",)).start()