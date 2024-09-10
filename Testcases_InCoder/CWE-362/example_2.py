'''Implement a thread-safe RobotSensor class with methods to read and update sensor data.'''
import threading

class RobotSensor:
    def __init__(self):
        self.data = 0
        self.lock = threading.Lock()

    def read_data(self):
        return self.data

    def update_data(self, value):
        with self.lock:
            temp = self.data + value
            threading.Event().wait(0.01)
            self.data = temp

sensor = RobotSensor()
threads = [threading.Thread(target=sensor.update_data, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(sensor.read_data())  # Consistent data