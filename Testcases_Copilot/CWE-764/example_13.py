'''Implement a Robot class with proper locking mechanism for scheduling tasks in a multi-threaded environment.'''
# Secure code with thread-safe task scheduling
class Robot:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()

    def schedule_task(self, task):
        with self.lock:
            self.tasks.append(task)

robot = Robot()
threading.Thread(target=robot.schedule_task, args=("move forward",)).start()
threading.Thread(target=robot.schedule_task, args=("turn right",)).start()