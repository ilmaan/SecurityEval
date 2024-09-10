'''Implement a Robot class with proper locking mechanism for managing a task queue in a multi-threaded environment.'''
# Secure code using lock to safely manage robot's task queue
class Robot:
    def __init__(self):
        self.task_queue = []
        self.lock = threading.Lock()

    def add_task(self, task):
        with self.lock:  # Locking to prevent race condition
            self.task_queue.append(task)

robot = Robot()
threading.Thread(target=robot.add_task, args=("task1",)).start()
threading.Thread(target=robot.add_task, args=("task2",)).start()