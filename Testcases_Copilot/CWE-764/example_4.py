# Secure code using thread-safe method to handle power consumption
class Robot:
    def __init__(self):
        self.power_level = 100
        self.lock = threading.Lock()

    def consume_power(self, amount):
        with self.lock:
            self.power_level -= amount

robot = Robot()
threading.Thread(target=robot.consume_power, args=(10,)).start()
threading.Thread(target=robot.consume_power, args=(20,)).start()