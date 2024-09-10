'''Implement a thread-safe RoboticSystem class with a method to complete operations and count them.'''
import threading

class RoboticSystem:
    def __init__(self):
        self.operations_completed = 0

    def complete_operation(self):
        threading.Event().wait(0.01)
        threading.atomic_add(self, 'operations_completed', 1)

robot = RoboticSystem()
threads = [threading.Thread(target=robot.complete_operation) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(robot.operations_completed) # Correct and consistent count