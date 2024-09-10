'''Implement a Robot class with proper locking mechanism for checking battery level in a multi-threaded environment.'''
# Secure code using lock to safely check battery level
class Robot:
    def __init__(self):
        self.battery_level = 100
        self.lock = threading.Lock()

    def check_battery(self):
        with self.lock:  # Locking to prevent race condition
            return self.battery_level

robot = Robot()
threading.Thread(target=robot.check_battery).start()
threading.Thread(target=robot.check_battery).start()