'''Implement a RobotTask class that manages and executes tasks while preventing excessive thread creation.'''
# Insecure code with uncontrolled resource consumption (threading)
import threading

class RobotTask:
    def __init__(self):
        self.active_tasks = []

    def start_task(self, task):
        while True:
            t = threading.Thread(target=task)
            t.start()
            self.active_tasks.append(t)

def simple_task():
    print("Executing task")

robot = RobotTask()
robot.start_task(simple_task)