# Secure code using deque to limit memory usage (fixed-size buffer)
from collections import deque

class SensorDataProcessor:
    def __init__(self, max_data=1000):
        self.data = deque(maxlen=max_data)

    def process_data(self, new_data):
        self.data.append(new_data)

processor = SensorDataProcessor()
processor.process_data("sensor_data")