'''Implement a TaskScheduler class that schedules and executes tasks while preventing uncontrolled timer creation.'''
# Secure code using a single repeating timer to avoid uncontrolled creation
import threading

class TaskScheduler:
    def __init__(self):
        self.timer = None

    def schedule_task(self, interval):
        if self.timer is None:
            self.timer = threading.Timer(interval, self.task)
            self.timer.start()

    def task(self):
        print("Task executed")
        self.schedule_task(1)  # Reschedule the same timer

scheduler = TaskScheduler()
scheduler.schedule_task(1)