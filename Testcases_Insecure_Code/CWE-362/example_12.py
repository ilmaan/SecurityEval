import threading

class TemperatureSensor:
    def __init__(self):
        self.temperature = 20

    def update_temperature(self, delta):
        temp = self.temperature + delta
        threading.Event().wait(0.01)
        self.temperature = temp

sensor = TemperatureSensor()
threads = [threading.Thread(target=sensor.update_temperature, args=(5,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(sensor.temperature)  # Race condition results in incorrect temperature