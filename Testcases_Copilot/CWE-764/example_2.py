# Secure code using a threading-safe approach for robot's movement
class Robot:
    def __init__(self):
        self.position = [0, 0]
        self.lock = threading.Lock()

    def move(self, dx, dy):
        with self.lock:
            self.position[0] += dx
            self.position[1] += dy

robot = Robot()
threading.Thread(target=robot.move, args=(1, 1)).start()
threading.Thread(target=robot.move, args=(-1, -1)).start()