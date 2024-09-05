# Secure code using lock to safely read sensor data
class Robot:
    def __init__(self):
        self.sensor_data = {}
        self.lock = threading.Lock()

    def read_sensor(self, sensor):
        with self.lock:  # Locking to prevent data inconsistency
            return self.sensor_data.get(sensor, 0)

robot = Robot()
threading.Thread(target=robot.read_sensor, args=("temperature",)).start()
threading.Thread(target=robot.read_sensor, args=("pressure",)).start()