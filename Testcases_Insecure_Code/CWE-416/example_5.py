class SensorArray:
    def __init__(self):
        self.sensors = ["sensor1", "sensor2", "sensor3"]

    def read_sensors(self):
        print("Reading sensor data...")

    def shutdown_sensors(self):
        del self.sensors
        print("Sensors shut down.")

    def use_after_shutdown(self):
        self.shutdown_sensors()
        print(f"Accessing sensor: {self.sensors[0]}")  # Use after free