'''Implement a Robot class with proper locking mechanism for updating sensor data in a multi-threaded environment.'''
# Secure code using lock to ensure safe access to sensor data
class Robot:
    def __init__(self):
        self.sensor_data = {}
        self.lock = threading.Lock()

    def update_sensor_data(self, sensor, data):
        with self.lock:  # Locking to prevent race condition
            self.sensor_data[sensor] = data

robot = Robot()
threading.Thread(target=robot.update_sensor_data, args=("camera", "data1")).start()
threading.Thread(target=robot.update_sensor_data, args=("camera", "data2")).start()