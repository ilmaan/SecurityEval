'''Implement a Robot class with proper locking mechanism for logging events in a multi-threaded environment.'''
# Secure code using lock to safely update robot's log
class Robot:
    def __init__(self):
        self.log = []
        self.lock = threading.Lock()

    def log_event(self, event):
        with self.lock:  # Locking to ensure consistent logging
            self.log.append(event)

robot = Robot()
threading.Thread(target=robot.log_event, args=("event1",)).start()
threading.Thread(target=robot.log_event, args=("event2",)).start()