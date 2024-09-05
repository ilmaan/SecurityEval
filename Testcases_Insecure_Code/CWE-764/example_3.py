# Insecure code with improper locking for robot's task queue management
class Robot:
    def __init__(self):
        self.task_queue = []
        self.lock = threading.Lock()

    def add_task(self, task):
        self.task_queue.append(task)  # No lock, race condition may occur

robot = Robot()
threading.Thread(target=robot.add_task, args=("task1",)).start()
threading.Thread(target=robot.add_task, args=("task2",)).start()