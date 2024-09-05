# Insecure code with uncontrolled resource consumption (timers)
import threading

class TaskScheduler:
    def __init__(self):
        self.timers = []

    def schedule_task(self, interval):
        while True:
            t = threading.Timer(interval, self.task)
            t.start()
            self.timers.append(t)

    def task(self):
        print("Task executed")

scheduler = TaskScheduler()
scheduler.schedule_task(1)