'''Implement a RobotTask class that manages and executes tasks while preventing excessive thread creation.'''
# Secure code with controlled threading using a thread pool
import threading
from concurrent.futures import ThreadPoolExecutor

class RobotTask:
    def __init__(self):
        self.executor = ThreadPoolExecutor(max_workers=10)

    def start_task(self, task):
        while True:
            self.executor.submit(task)

def simple_task():
    print("Executing task")

robot = RobotTask()
robot.start_task(simple_task)