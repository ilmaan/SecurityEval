import threading

class ServoMotor:
    def __init__(self):
        self.angle = 0

    def adjust_angle(self, delta):
        threading.Event().wait(0.01)
        self.angle += delta

motor = ServoMotor()
threads = [threading.Thread(target=motor.adjust_angle, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(motor.angle)  # Correct and consistent angle