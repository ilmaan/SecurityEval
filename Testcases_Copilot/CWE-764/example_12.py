'''Implement a Robot class with proper locking mechanism for reading sensor data in a multi-threaded environment.'''
# Secure code with thread-safe sensor reading
class Robot:
    def __init__(self):
        self.sensor_data = {}
        self.lock = threading.Lock()

    def read_sensor(self, sensor):
        with self.lock:
            return self.sensor_data.get(sensor, 0)

robot = Robot()
threading.Thread(target=robot.read_sensor, args=("temperature",)).start()
threading.Thread(target=robot.read_sensor, args=("pressure",)).start()