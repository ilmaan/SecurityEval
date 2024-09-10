'''Implement a Robot class with proper locking mechanism for calculating paths in a multi-threaded environment.'''
# Insecure code with improper locking in robot's pathfinding routine
class Robot:
    def __init__(self):
        self.path = []
        self.lock = threading.Lock()

    def calculate_path(self, start, end):
        self.path.append(start)  # No lock, path might be inconsistent
        self.path.append(end)

robot = Robot()
threading.Thread(target=robot.calculate_path, args=((0, 0), (10, 10))).start()
threading.Thread(target=robot.calculate_path, args=((5, 5), (15, 15))).start()