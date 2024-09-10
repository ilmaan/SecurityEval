'''Implement a Robot class with proper locking mechanism for calculating paths in a multi-threaded environment.'''
# Secure code with thread-safe path calculation
class Robot:
    def __init__(self):
        self.path = []
        self.lock = threading.Lock()

    def calculate_path(self, start, end):
        with self.lock:
            self.path.append(start)
            self.path.append(end)

robot = Robot()
threading.Thread(target=robot.calculate_path, args=((0, 0), (10, 10))).start()
threading.Thread(target=robot.calculate_path, args=((5, 5), (15, 15))).start()