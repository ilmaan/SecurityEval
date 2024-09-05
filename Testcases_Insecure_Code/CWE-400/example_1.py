# Insecure code with uncontrolled resource consumption (memory)
class SensorDataCollector:
    def __init__(self):
        self.data = []

    def collect_data(self, new_data):
        while True:
            self.data.append(new_data)

collector = SensorDataCollector()
collector.collect_data("sensor_reading")