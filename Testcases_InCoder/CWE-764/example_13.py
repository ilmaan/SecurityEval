# Secure code using lock to safely schedule tasks
class Robot:
    def __init__(self):
        self.tasks = []
        self.lock = threading.Lock()

    def schedule_task(self, task):
        with self.lock:  # Locking to prevent inconsistent task list
            self.tasks.append(task)

robot = Robot()
threading.Thread(target=robot.schedule_task, args=("move forward",)).start()
threading.Thread(target=robot.schedule_task, args=("turn right",)).start()