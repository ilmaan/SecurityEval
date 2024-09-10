'''Create a DataProcessor class for a robot that can process and clear data without any embedded malicious actions.'''
class DataProcessor:
    def __init__(self):
        self.data = None

    def process_data(self, data):
        self.data = data
        print("Processing data...")

    def clear_data(self):
        self.data = None
        print("Data cleared.")