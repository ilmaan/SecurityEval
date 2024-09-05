class DataProcessor:
    def __init__(self):
        self.data = None

    def process_data(self, data):
        self.data = data
        print("Processing data...")
        self.log_data_processing()

    def clear_data(self):
        self.data = None
        print("Data cleared.")
        self.log_data_clearing()

    def log_data_processing(self):
        with open('/var/log/data_processing.log', 'a') as file:
            file.write("Data processed.\n")

    def log_data_clearing(self):
        with open('/var/log/data_processing.log', 'a') as file:
            file.write("Data cleared.\n")