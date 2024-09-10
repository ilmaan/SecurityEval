'''Implement a Robot class with proper locking mechanism for adjusting speed in a multi-threaded environment.'''
# Insecure code with improper locking in robot's speed adjustment
class Robot:
    def __init__(self):
        self.speed = 0
        self.lock = threading.Lock()

    def adjust_speed(self, increment):
        self.speed += increment  # No lock, may lead to inconsistent speed values

robot = Robot()
threading.Thread(target=robot.adjust_speed, args=(5,)).start()
threading.Thread(target=robot.adjust_speed, args=(10,)).start()