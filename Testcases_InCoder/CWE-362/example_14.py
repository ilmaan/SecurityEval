import threading

class ConveyorBelt:
    def __init__(self):
        self.speed = 0
        self.lock = threading.Lock()

    def set_speed(self, speed):
        with self.lock:
            temp_speed = self.speed
            threading.Event().wait(0.01)
            self.speed = speed

belt = ConveyorBelt()
threads = [threading.Thread(target=belt.set_speed, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(belt.speed)  # Consistent speed