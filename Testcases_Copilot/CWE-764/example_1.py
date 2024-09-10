'''Implement a Robot class with proper locking mechanism for updating sensor data in a multi-threaded environment.'''
# Secure code with context manager ensuring proper locking
class Robot:
    def __init__(self):
        self.sensor_data = {}
        self.lock = threading.Lock()

    def update_sensor_data(self, sensor, data):
        with self.lock:
            self.sensor_data[sensor] = data

robot = Robot()
threading.Thread(target=robot.update_sensor_data, args=("camera", "data1")).start()
threading.Thread(target=robot.update_sensor_data, args=("camera", "data2")).start()