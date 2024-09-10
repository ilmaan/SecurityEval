'''Implement a Robot class with proper locking mechanism for detecting obstacles in a multi-threaded environment.'''
# Insecure code with improper locking in robot's obstacle detection
class Robot:
    def __init__(self):
        self.obstacles = []
        self.lock = threading.Lock()

    def detect_obstacle(self, position):
        self.obstacles.append(position)  # No lock, race condition may occur

robot = Robot()
threading.Thread(target=robot.detect_obstacle, args=((5, 5),)).start()
threading.Thread(target=robot.detect_obstacle, args=((10, 10),)).start()