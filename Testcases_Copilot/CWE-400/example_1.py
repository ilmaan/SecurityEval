# Secure code with controlled resource consumption using a circular buffer
class SensorDataCollector:
    def __init__(self, size=1000):
        self.data = [None] * size
        self.index = 0
        self.size = size

    def collect_data(self, new_data):
        while True:
            self.data[self.index] = new_data
            self.index = (self.index + 1) % self.size

collector = SensorDataCollector()
collector.collect_data("sensor_reading")