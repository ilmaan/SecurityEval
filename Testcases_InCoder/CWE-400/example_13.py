'''Implement a CommandSender class that sends commands with a retry mechanism while preventing uncontrolled retry attempts.'''
# Secure code with limited retries (using a counter)
class CommandSender:
    def __init__(self, max_retries=5):
        self.max_retries = max_retries

    def send_command(self, command):
        retries = 0
        while retries < self.max_retries:
            try:
                result = self.simulate_send(command)
                break
            except Exception as e:
                retries += 1
                print(f"Command failed, retrying... ({retries}/{self.max_retries})")

    def simulate_send(self, command):
        raise Exception("Simulated failure")

sender = CommandSender()
sender.send_command("START")