class LogHandler:
    def __init__(self):
        self.logs = ["log1", "log2", "log3"]

    def save_logs(self):
        print("Saving logs...")

    def clear_logs(self):
        del self.logs
        print("Logs cleared.")

    def complete_saving(self):
        self.save_logs()
        self.clear_logs()
        # Avoid accessing `self.logs` after they have been cleared