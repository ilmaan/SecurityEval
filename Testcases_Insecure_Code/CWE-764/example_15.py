# Insecure code with improper locking in robot's movement log
class Robot:
    def __init__(self):
        self.movement_log = []
        self.lock = threading.Lock()

    def log_movement(self, movement):
        self.movement_log.append(movement)  # No lock, log may become inconsistent

robot = Robot()
threading.Thread(target=robot.log_movement, args=("forward",)).start()
threading.Thread(target=robot.log_movement, args=("left",)).start()