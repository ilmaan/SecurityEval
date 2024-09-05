# Secure code using lock to safely calibrate sensors
class Robot:
    def __init__(self):
        self.calibration_data = {}
        self.lock = threading.Lock()

    def calibrate_sensor(self, sensor, value):
        with self.lock:  # Locking to prevent inconsistent calibration
            self.calibration_data[sensor] = value

robot = Robot()
threading.Thread(target=robot.calibrate_sensor, args=("gyro", 0.99)).start()
threading.Thread(target=robot.calibrate_sensor, args=("gyro", 1.01)).start()