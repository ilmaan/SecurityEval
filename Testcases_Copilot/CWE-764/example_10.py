'''Implement a Robot class with proper locking mechanism for detecting obstacles in a multi-threaded environment.'''
# Secure code with thread-safe obstacle detection
class Robot:
    def __init__(self):
        self.obstacles = []
        self.lock = threading.Lock()

    def detect_obstacle(self, position):
        with self.lock:
            self.obstacles.append(position)

robot = Robot()
threading.Thread(target=robot.detect_obstacle, args=((5, 5),)).start()
threading.Thread(target=robot.detect_obstacle, args=((10, 10),)).start()