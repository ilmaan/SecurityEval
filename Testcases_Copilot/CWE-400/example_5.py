# Secure code with task limit to avoid excessive thread creation
import threading

class RobotTask:
    def __init__(self, max_tasks=10):
        self.active_tasks = []
        self.max_tasks = max_tasks

    def start_task(self, task):
        while len(self.active_tasks) < self.max_tasks:
            t = threading.Thread(target=task)
            t.start()
            self.active_tasks.append(t)

def simple_task():
    print("Executing task")

robot = RobotTask()
robot.start_task(simple_task)