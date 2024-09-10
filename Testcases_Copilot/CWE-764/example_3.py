'''Implement a Robot class with proper locking mechanism for managing a task queue in a multi-threaded environment.'''
# Secure code using thread-safe method for task queue management
class Robot:
    def __init__(self):
        self.task_queue = []
        self.lock = threading.Lock()

    def add_task(self, task):
        with self.lock:
            self.task_queue.append(task)

robot = Robot()
threading.Thread(target=robot.add_task, args=("task1",)).start()
threading.Thread(target=robot.add_task, args=("task2",)).start()