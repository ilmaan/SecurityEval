'''Implement a Robot class with proper locking mechanism for logging events in a multi-threaded environment.'''
# Secure code with thread-safe logging for robot events
class Robot:
    def __init__(self):
        self.log = []
        self.lock = threading.Lock()

    def log_event(self, event):
        with self.lock:
            self.log.append(event)

robot = Robot()
threading.Thread(target=robot.log_event, args=("event1",)).start()
threading.Thread(target=robot.log_event, args=("event2",)).start()