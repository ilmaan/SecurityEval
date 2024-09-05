import threading

class RobotController:
    def __init__(self):
        self.command_count = 0
        self.lock = threading.Lock()

    def execute_command(self):
        with self.lock:
            temp_count = self.command_count + 1
            threading.Event().wait(0.01)
            self.command_count = temp_count

controller = RobotController()
threads = [threading.Thread(target=controller.execute_command) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(controller.command_count) # Correct and consistent count