# Secure code using lock to safely calculate robot's path
class Robot:
    def __init__(self):
        self.path = []
        self.lock = threading.Lock()

    def calculate_path(self, start, end):
        with self.lock:  # Locking to prevent inconsistent path
            self.path.append(start)
            self.path.append(end)

robot = Robot()
threading.Thread(target=robot.calculate_path, args=((0, 0), (10, 10))).start()
threading.Thread(target=robot.calculate_path, args=((5, 5), (15, 15))).start()