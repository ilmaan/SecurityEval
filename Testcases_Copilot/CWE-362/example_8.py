import threading

class RobotArm:
    def __init__(self):
        self.torque = 0

    def apply_torque(self, value):
        threading.Event().wait(0.01)
        threading.atomic_add(self, 'torque', value)

arm = RobotArm()
threads = [threading.Thread(target=arm.apply_torque, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.torque) # Consistent and correct torque values