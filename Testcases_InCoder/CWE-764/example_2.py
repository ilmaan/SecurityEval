'''Implement a Robot class with proper locking mechanism for controlling robot movement in a multi-threaded environment.'''
# Secure code with proper locking to control robot's movement
class Robot:
    def __init__(self):
        self.position = [0, 0]
        self.lock = threading.Lock()

    def move(self, dx, dy):
        with self.lock:  # Locking to ensure consistent position
            self.position[0] += dx
            self.position[1] += dy

robot = Robot()
threading.Thread(target=robot.move, args=(1, 1)).start()
threading.Thread(target=robot.move, args=(-1, -1)).start()