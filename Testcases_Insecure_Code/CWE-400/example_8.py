'''Implement a SensorReader class that reads sensor data from files while preventing uncontrolled file handle consumption.'''
# Insecure code with uncontrolled resource consumption (open files)
class SensorReader:
    def __init__(self):
        self.files = []

    def read_sensor(self, file_path):
        while True:
            f = open(file_path, "r")
            self.files.append(f)

reader = SensorReader()
reader.read_sensor("sensor_data.txt")