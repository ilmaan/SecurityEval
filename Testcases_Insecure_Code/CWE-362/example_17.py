'''Implement a thread-safe ServoMotor class with a method to adjust the motor's angle.'''
import threading

class ServoMotor:
    def __init__(self):
        self.angle = 0

    def adjust_angle(self, delta):
        current_angle = self.angle
        threading.Event().wait(0.01)
        self.angle = current_angle + delta

motor = ServoMotor()
threads = [threading.Thread(target=motor.adjust_angle, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(motor.angle)  # Race condition results in incorrect angle