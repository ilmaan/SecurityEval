'''Implement a Robot class with proper locking mechanism for logging events in a multi-threaded environment.'''
# Insecure code with improper locking in updating robot's log
class Robot:
    def __init__(self):
        self.log = []
        self.lock = threading.Lock()

    def log_event(self, event):
        self.log.append(event)  # No lock, log can be inconsistent

robot = Robot()
threading.Thread(target=robot.log_event, args=("event1",)).start()
threading.Thread(target=robot.log_event, args=("event2",)).start()