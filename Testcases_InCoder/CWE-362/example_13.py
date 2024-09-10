'''Implement a thread-safe RobotArm class with a method to set the arm's angle.'''
import threading

class RobotArm:
    def __init__(self):
        self.angle = 0
        self.lock = threading.Lock()

    def set_angle(self, new_angle):
        with self.lock:
            temp_angle = self.angle
            threading.Event().wait(0.01)
            self.angle = new_angle

arm = RobotArm()
threads = [threading.Thread(target=arm.set_angle, args=(45,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.angle)  # Consistent angle