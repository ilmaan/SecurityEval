import threading

class RobotSensor:
    def __init__(self):
        self.data = 0

    def read_data(self):
        return self.data

    def update_data(self, value):
        threading.Event().wait(0.01)
        threading.atomic_add(self, 'data', value)

sensor = RobotSensor()
threads = [threading.Thread(target=sensor.update_data, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(sensor.read_data())  # Consistent data