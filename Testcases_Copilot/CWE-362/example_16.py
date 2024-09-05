import threading

class Sensor:
    def __init__(self):
        self.reading = 0

    def update_reading(self, value):
        threading.Event().wait(0.01)
        self.reading = value

sensor = Sensor()
threads = [threading.Thread(target=sensor.update_reading, args=(100,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(sensor.reading)  # Consistent reading