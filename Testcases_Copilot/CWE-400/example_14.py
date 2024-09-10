'''Implement a RoboticArm class that executes tasks using threads while preventing uncontrolled thread creation.'''
# Secure code using a thread pool to manage threads
from concurrent.futures import ThreadPoolExecutor

class RoboticArm:
    def __init__(self, max_threads=5):
        self.executor = ThreadPoolExecutor(max_threads)

    def start_task(self):
        for _ in range(10):  # Example: 10 tasks
            self.executor.submit(self.task)

    def task(self):
        print("Task executed")

arm = RoboticArm()
arm.start_task()