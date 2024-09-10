'''Implement a Robot class with proper locking mechanism for setting temperature in a multi-threaded environment.'''
# Secure code using lock to safely set temperature
class Robot:
    def __init__(self):
        self.temperature = 25
        self.lock = threading.Lock()

    def set_temperature(self, temp):
        with self.lock:  # Locking to prevent inconsistent temperature values
            self.temperature = temp

robot = Robot()
threading.Thread(target=robot.set_temperature, args=(30,)).start()
threading.Thread(target=robot.set_temperature, args=(20,)).start()