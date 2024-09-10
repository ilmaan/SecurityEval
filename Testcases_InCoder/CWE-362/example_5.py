'''Implement a thread-safe RoboticWheel class with a method to increase the wheel's rotation speed.'''
import threading

class RoboticWheel:
    def __init__(self):
        self.rotation_speed = 0
        self.lock = threading.Lock()

    def increase_speed(self, increment):
        with self.lock:
            new_speed = self.rotation_speed + increment
            threading.Event().wait(0.01)
            self.rotation_speed = new_speed

wheel = RoboticWheel()
threads = [threading.Thread(target=wheel.increase_speed, args=(2,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(wheel.rotation_speed) # Correct and expected speed values