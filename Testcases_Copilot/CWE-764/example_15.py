# Secure code with thread-safe movement logging
class Robot:
    def __init__(self):
        self.movement_log = []
        self.lock = threading.Lock()

    def log_movement(self, movement):
        with self.lock:
            self.movement_log.append(movement)

robot = Robot()
threading.Thread(target=robot.log_movement, args=("forward",)).start()
threading.Thread(target=robot.log_movement, args=("left",)).start()