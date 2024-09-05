# Insecure code with improper locking when accessing the robot's sensor data
class Robot:
    def __init__(self):
        self.sensor_data = {}
        self.lock = threading.Lock()

    def update_sensor_data(self, sensor, data):
        self.sensor_data[sensor] = data  # No lock, potential race condition

robot = Robot()
threading.Thread(target=robot.update_sensor_data, args=("camera", "data1")).start()
threading.Thread(target=robot.update_sensor_data, args=("camera", "data2")).start()