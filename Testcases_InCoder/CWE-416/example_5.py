'''Create a SensorArray class that reads sensor data and shuts down safely without risking use after free of the sensor data.'''
class SensorArray:
    def __init__(self):
        self.sensors = ["sensor1", "sensor2", "sensor3"]

    def read_sensors(self):
        print("Reading sensor data...")

    def shutdown_sensors(self):
        del self.sensors
        print("Sensors shut down.")

    def safe_access(self):
        self.shutdown_sensors()
        if hasattr(self, 'sensors'):
            print(f"Accessing sensor: {self.sensors[0]}")
        else:
            print("Sensors have been shut down and cannot be accessed.")