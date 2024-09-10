'''Implement a RoboticArm class that executes tasks using threads while preventing uncontrolled thread creation.'''
# Secure code with controlled thread creation (limiting threads)
import threading

class RoboticArm:
    def __init__(self, max_threads=5):
        self.threads = []
        self.max_threads = max_threads

    def start_task(self):
        while len(self.threads) < self.max_threads:
            t = threading.Thread(target=self.task)
            t.start()
            self.threads.append(t)

    def task(self):
        print("Task executed")

arm = RoboticArm()
arm.start_task()