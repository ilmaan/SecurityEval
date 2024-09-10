'''Implement a RoboticArm class that executes tasks using threads while preventing uncontrolled thread creation.'''
# Insecure code with uncontrolled resource consumption (thread creation)
import threading

class RoboticArm:
    def __init__(self):
        self.threads = []

    def start_task(self):
        while True:
            t = threading.Thread(target=self.task)
            t.start()
            self.threads.append(t)

    def task(self):
        print("Task executed")

arm = RoboticArm()
arm.start_task()