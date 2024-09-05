# Secure code with thread-safe temperature control
class Robot:
    def __init__(self):
        self.temperature = 25
        self.lock = threading.Lock()

    def set_temperature(self, temp):
        with self.lock:
            self.temperature = temp

robot = Robot()
threading.Thread(target=robot.set_temperature, args=(30,)).start()
threading.Thread(target=robot.set_temperature, args=(20,)).start()