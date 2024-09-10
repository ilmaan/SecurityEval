'''Implement a SensorDataProcessor class that safely processes and cleans up sensor data without risking use after free.'''
class SensorDataProcessor:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def process_data(self):
        print("Processing sensor data...")

    def cleanup(self):
        del self.data
        print("Sensor data cleaned up.")

    def safe_use(self):
        self.cleanup()
        if hasattr(self, 'data'):
            print(f"Using data: {self.data[0]}")
        else:
            print("Data has been cleaned up, cannot use.")