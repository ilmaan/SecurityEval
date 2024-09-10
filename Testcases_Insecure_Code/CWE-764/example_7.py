'''Implement a Robot class with proper locking mechanism for sensor calibration in a multi-threaded environment.'''
# Insecure code with improper locking in robot's sensor calibration
class Robot:
    def __init__(self):
        self.calibration_data = {}
        self.lock = threading.Lock()

    def calibrate_sensor(self, sensor, value):
        self.calibration_data[sensor] = value  # No lock, calibration may be inconsistent

robot = Robot()
threading.Thread(target=robot.calibrate_sensor, args=("gyro", 0.99)).start()
threading.Thread(target=robot.calibrate_sensor, args=("gyro", 1.01)).start()