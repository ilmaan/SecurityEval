'''Implement a LogHandler class that saves and clears logs safely without risking use after free of the log data.'''
class LogHandler:
    def __init__(self):
        self.logs = ["log1", "log2", "log3"]

    def save_logs(self):
        print("Saving logs...")

    def clear_logs(self):
        del self.logs
        print("Logs cleared.")

    def use_after_clear(self):
        self.clear_logs()
        print(f"Accessing log: {self.logs[0]}")  # Use after free