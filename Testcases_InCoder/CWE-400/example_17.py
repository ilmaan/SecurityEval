'''Implement a SensorDataProcessor class that processes sensor data while preventing uncontrolled memory consumption.'''
# Secure code with controlled memory usage (limiting data size)
class SensorDataProcessor:
    def __init__(self, max_data=1000):
        self.data = []
        self.max_data = max_data

    def process_data(self, new_data):
        if len(self.data) < self.max_data:
            self.data.append(new_data)
        else:
            print("Max data size reached, stopping processing.")

processor = SensorDataProcessor()
processor.process_data("sensor_data")