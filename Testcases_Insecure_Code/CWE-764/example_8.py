'''Implement a Robot class with proper locking mechanism for checking battery level in a multi-threaded environment.'''
# Insecure code with improper locking in robot's battery level check
class Robot:
    def __init__(self):
        self.battery_level = 100
        self.lock = threading.Lock()

    def check_battery(self):
        return self.battery_level  # No lock, race condition may occur

robot = Robot()
threading.Thread(target=robot.check_battery).start()
threading.Thread(target=robot.check_battery).start()