'''Create a thread-safe RobotControl class with a method to set the robot's status.'''
import threading

class RobotControl:
    def __init__(self):
        self.status = "Idle"

    def set_status(self, new_status):
        threading.Event().wait(0.01)
        threading.atomic_exchange(self, 'status', new_status)

robot = RobotControl()
threads = [threading.Thread(target=robot.set_status, args=("Active",)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(robot.status)  # Consistent and expected status