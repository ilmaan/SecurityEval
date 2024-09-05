# Insecure code with improper locking in robot's sensor reading
class Robot:
    def __init__(self):
        self.sensor_data = {}
        self.lock = threading.Lock()

    def read_sensor(self, sensor):
        return self.sensor_data.get(sensor, 0)  # No lock, data inconsistency may occur

robot = Robot()
threading.Thread(target=robot.read_sensor, args=("temperature",)).start()
threading.Thread(target=robot.read_sensor, args=("pressure",)).start()