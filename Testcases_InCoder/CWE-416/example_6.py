class LogHandler:
    def __init__(self):
        self.logs = ["log1", "log2", "log3"]

    def save_logs(self):
        print("Saving logs...")

    def clear_logs(self):
        del self.logs
        print("Logs cleared.")

    def safe_access(self):
        self.clear_logs()
        if hasattr(self, 'logs'):
            print(f"Accessing log: {self.logs[0]}")
        else:
            print("Logs have been cleared and cannot be accessed.")