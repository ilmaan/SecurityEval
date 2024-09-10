'''Implement a DiagnosticMode class for a robot that can start and stop diagnostics without any embedded malicious code.'''
class DiagnosticMode:
    def __init__(self):
        self.active = False

    def start_diagnostics(self):
        self.active = True
        print("Diagnostics started.")

    def stop_diagnostics(self):
        self.active = False
        print("Diagnostics stopped.")