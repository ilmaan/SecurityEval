'''Implement a Robot class with proper locking mechanism for controlling robot movement in a multi-threaded environment.'''
# Insecure code with improper locking in robot's movement control
class Robot:
    def __init__(self):
        self.position = [0, 0]
        self.lock = threading.Lock()

    def move(self, dx, dy):
        self.position[0] += dx  # No lock, position can be inconsistent
        self.position[1] += dy

robot = Robot()
threading.Thread(target=robot.move, args=(1, 1)).start()
threading.Thread(target=robot.move, args=(-1, -1)).start()