import threading

class RobotArm:
    def __init__(self):
        self.speed = 0

    def set_speed(self, speed):
        temp_speed = self.speed
        threading.Event().wait(0.01)
        self.speed = speed

arm = RobotArm()
threads = [threading.Thread(target=arm.set_speed, args=(20,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.speed)  # Race condition causes inconsistent speed