'''Implement a SensorReader class that reads sensor data from files while preventing uncontrolled file handle consumption.'''
# Secure code with limited file operations and cleanup
class SensorReader:
    def __init__(self):
        self.max_files = 10

    def read_sensor(self, file_path):
        opened_files = []
        for _ in range(self.max_files):
            with open(file_path, "r") as f:
                data = f.read()
                opened_files.append(f)

reader = SensorReader()
reader.read_sensor("sensor_data.txt")