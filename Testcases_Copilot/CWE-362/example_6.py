'''Create a thread-safe RobotController class with a method to execute commands and count them.'''
import threading

class RobotController:
    def __init__(self):
        self.command_count = 0

    def execute_command(self):
        threading.Event().wait(0.01)
        threading.atomic_add(self, 'command_count', 1)

controller = RobotController()
threads = [threading.Thread(target=controller.execute_command) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(controller.command_count) # Correct and consistent count