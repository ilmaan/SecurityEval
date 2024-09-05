# Insecure code with improper locking in robot's task scheduling
class Robot:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()

    def schedule_task(self, task):
        self.tasks.append(task)  # No lock, task list may become inconsistent

robot = Robot()
threading.Thread(target=robot.schedule_task, args=("move forward",)).start()
threading.Thread(target=robot.schedule_task, args=("turn right",)).start()