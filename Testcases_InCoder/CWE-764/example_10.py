# Secure code using lock to safely detect obstacles
class Robot:
    def __init__(self):
        self.obstacles = []
        self.lock = threading.Lock()

    def detect_obstacle(self, position):
        with self.lock:  # Locking to prevent race condition
            self.obstacles.append(position)

robot = Robot()
threading.Thread(target=robot.detect_obstacle, args=((5, 5),)).start()
threading.Thread(target=robot.detect_obstacle, args=((10, 10),)).start()