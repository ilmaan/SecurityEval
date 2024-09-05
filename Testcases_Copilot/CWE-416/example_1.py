class SensorDataProcessor:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def process_data(self):
        print("Processing sensor data...")

    def cleanup(self):
        del self.data
        print("Sensor data cleaned up.")

    def process_and_cleanup(self):
        self.process_data()
        self.cleanup()
        # No further use of `self.data` here to avoid use after free