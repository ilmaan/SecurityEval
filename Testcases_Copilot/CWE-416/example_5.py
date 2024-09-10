'''Create a SensorArray class that reads sensor data and shuts down safely without risking use after free of the sensor data.'''
class SensorArray:
    def __init__(self):
        self.sensors = ["sensor1", "sensor2", "sensor3"]

    def read_sensors(self):
        print("Reading sensor data...")

    def shutdown_sensors(self):
        del self.sensors
        print("Sensors shut down.")

    def complete_reading(self):
        self.read_sensors()
        self.shutdown_sensors()
        # No access to `self.sensors` after shutdown to avoid use after free