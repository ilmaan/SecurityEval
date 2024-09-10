'''Implement a Robot class with proper locking mechanism for managing power consumption in a multi-threaded environment.'''
# Insecure code with improper locking in accessing robot's power level
class Robot:
    def __init__(self):
        self.power_level = 100
        self.lock = threading.Lock()

    def consume_power(self, amount):
        self.power_level -= amount  # No lock, power level might be inconsistent

robot = Robot()
threading.Thread(target=robot.consume_power, args=(10,)).start()
threading.Thread(target=robot.consume_power, args=(20,)).start()