# Secure code with thread-safe battery level check
class Robot:
    def __init__(self):
        self.battery_level = 100
        self.lock = threading.Lock()

    def check_battery(self):
        with self.lock:
            return self.battery_level

robot = Robot()
threading.Thread(target=robot.check_battery).start()
threading.Thread(target=robot.check_battery).start()