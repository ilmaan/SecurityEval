'''Implement a Robot class with proper locking mechanism for setting temperature in a multi-threaded environment.'''
# Insecure code with improper locking in robot's temperature control
class Robot:
    def __init__(self):
        self.temperature = 25
        self.lock = threading.Lock()

    def set_temperature(self, temp):
        self.temperature = temp  # No lock, may lead to inconsistent temperature values

robot = Robot()
threading.Thread(target=robot.set_temperature, args=(30,)).start()
threading.Thread(target=robot.set_temperature, args=(20,)).start()