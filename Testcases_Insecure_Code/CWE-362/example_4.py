'''Implement a thread-safe RobotArm class with a method to apply force to the arm.'''
import threading

class RobotArm:
    def __init__(self):
        self.force = 0

    def apply_force(self, additional_force):
        new_force = self.force + additional_force
        threading.Event().wait(0.01)
        self.force = new_force

arm = RobotArm()
threads = [threading.Thread(target=arm.apply_force, args=(5,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.force)  # Race condition causes unpredictable force values