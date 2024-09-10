'''Implement a Robot class with proper locking mechanism for managing power consumption in a multi-threaded environment.'''
# Secure code using locking mechanism to safely access power level
class Robot:
    def __init__(self):
        self.power_level = 100
        self.lock = threading.Lock()

    def consume_power(self, amount):
        with self.lock:  # Locking to ensure consistent power level
            self.power_level -= amount

robot = Robot()
threading.Thread(target=robot.consume_power, args=(10,)).start()
threading.Thread(target=robot.consume_power, args=(20,)).start()