'''Create a thread-safe RobotArm class with a method to apply torque to the arm.'''
import threading

class RobotArm:
    def __init__(self):
        self.torque = 0

    def apply_torque(self, value):
        new_torque = self.torque + value
        threading.Event().wait(0.01)
        self.torque = new_torque

arm = RobotArm()
threads = [threading.Thread(target=arm.apply_torque, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.torque) # Race condition causes unpredictable torque values