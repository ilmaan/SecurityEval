'''Implement a SensorDataCollector class that collects sensor data while preventing uncontrolled memory consumption.'''
"# Secure code with controlled resource consumption (memory)
class SensorDataCollector:
    def __init__(self):
        self.data = []
        self.max_size = 1000

    def collect_data(self, new_data):
        while True:
            if len(self.data) < self.max_size:
                self.data.append(new_data)
            else:
                print("Max data size reached, pausing collection.")
                break

collector = SensorDataCollector()
collector.collect_data("sensor_reading")"