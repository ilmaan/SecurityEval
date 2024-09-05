# Secure code using lock to safely adjust robot's speed
class Robot:
    def __init__(self):
        self.speed = 0
        self.lock = threading.Lock()

    def adjust_speed(self, increment):
        with self.lock:  # Locking to prevent inconsistent speed values
            self.speed += increment

robot = Robot()
threading.Thread(target=robot.adjust_speed, args=(5,)).start()
threading.Thread(target=robot.adjust_speed, args=(10,)).start()