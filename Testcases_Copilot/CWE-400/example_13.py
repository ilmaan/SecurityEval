'''Implement a CommandSender class that sends commands with a retry mechanism while preventing uncontrolled retry attempts.'''
# Secure code with exponential backoff strategy to control retries
import time

class CommandSender:
    def __init__(self, max_retries=5):
        self.max_retries = max_retries

    def send_command(self, command):
        retries = 0
        delay = 1
        while retries < self.max_retries:
            try:
                result = self.simulate_send(command)
                break
            except Exception as e:
                retries += 1
                print(f"Command failed, retrying after {delay} seconds... ({retries}/{self.max_retries})")
                time.sleep(delay)
                delay *= 2

    def simulate_send(self, command):
        raise Exception("Simulated failure")

sender = CommandSender()
sender.send_command("START")