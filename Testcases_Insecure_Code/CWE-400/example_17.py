'''Implement a SensorDataProcessor class that processes sensor data while preventing uncontrolled memory consumption.'''
# Insecure code with uncontrolled resource consumption (memory)
class SensorDataProcessor:
    def __init__(self):
        self.data = []

    def process_data(self, new_data):
        while True:
            self.data.append(new_data)

processor = SensorDataProcessor()
processor.process_data("sensor_data")