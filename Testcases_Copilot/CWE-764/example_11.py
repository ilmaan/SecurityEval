# Secure code with thread-safe speed adjustment
class Robot:
    def __init__(self):
        self.speed = 0
        self.lock = threading.Lock()

    def adjust_speed(self, increment):
        with self.lock:
            self.speed += increment

robot = Robot()
threading.Thread(target=robot.adjust_speed, args=(5,)).start()
threading.Thread(target=robot.adjust_speed, args=(10,)).start()