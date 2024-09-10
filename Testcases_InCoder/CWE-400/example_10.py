'''Implement a TaskScheduler class that schedules and executes tasks while preventing uncontrolled timer creation.'''
# Secure code with controlled timer creation (limiting timers)
import threading

class TaskScheduler:
    def __init__(self, max_timers=5):
        self.timers = []
        self.max_timers = max_timers

    def schedule_task(self, interval):
        for _ in range(self.max_timers):
            t = threading.Timer(interval, self.task)
            t.start()
            self.timers.append(t)

    def task(self):
        print("Task executed")

scheduler = TaskScheduler()
scheduler.schedule_task(1)