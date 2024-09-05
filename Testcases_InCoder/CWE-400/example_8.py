# Secure code with controlled file opening (using context manager)
class SensorReader:
    def __init__(self):
        pass

    def read_sensor(self, file_path):
        while True:
            with open(file_path, "r") as f:
                data = f.read()

reader = SensorReader()
reader.read_sensor("sensor_data.txt")