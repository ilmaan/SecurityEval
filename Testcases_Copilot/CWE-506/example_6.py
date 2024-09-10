'''Implement a DiagnosticMode class for a robot that can start and stop diagnostics without any embedded malicious code.'''
class DiagnosticMode:
    def __init__(self):
        self.active = False

    def start_diagnostics(self):
        self.active = True
        print("Diagnostics started.")
        self.log_diagnostics("Started")

    def stop_diagnostics(self):
        self.active = False
        print("Diagnostics stopped.")
        self.log_diagnostics("Stopped")

    def log_diagnostics(self, status):
        with open('/var/log/diagnostics.log', 'a') as file:
            file.write(f"Diagnostics {status}.\n")