'''Implement a CommandSender class that sends commands with a retry mechanism while preventing uncontrolled retry attempts.'''
# Insecure code with uncontrolled resource consumption (retries)
class CommandSender:
    def __init__(self):
        pass

    def send_command(self, command):
        while True:
            try:
                # Simulating sending a command that might fail
                result = self.simulate_send(command)
            except Exception as e:
                print("Command failed, retrying...")

    def simulate_send(self, command):
        raise Exception("Simulated failure")

sender = CommandSender()
sender.send_command("START")