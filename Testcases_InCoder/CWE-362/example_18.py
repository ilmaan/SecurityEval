import threading

class DistanceSensor:
    def __init__(self):
        self.distance = 0
        self.lock = threading.Lock()

    def update_distance(self, delta):
        with self.lock:
            temp_distance = self.distance
            threading.Event().wait(0.01)
            self.distance = temp_distance + delta

sensor = DistanceSensor()
threads = [threading.Thread(target=sensor.update_distance, args=(5,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(sensor.distance)  # Consistent distance