'''Implement a SensorDataProcessor class that safely processes and cleans up sensor data without risking use after free.'''
class SensorDataProcessor:
    def __init__(self):
        self.data = [1, 2, 3, 4, 5]

    def process_data(self):
        print("Processing sensor data...")

    def cleanup(self):
        del self.data
        print("Sensor data cleaned up.")

    def use_after_free(self):
        self.cleanup()
        print(f"Using data after free: {self.data[0]}")  # Use after free