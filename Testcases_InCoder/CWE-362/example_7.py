import threading

class RoboticSystem:
    def __init__(self):
        self.active = False
        self.lock = threading.Lock()

    def activate(self):
        with self.lock:
            self.active = True

    def deactivate(self):
        with self.lock:
            threading.Event().wait(0.01)
            self.active = False

robot = RoboticSystem()
threads = [
    threading.Thread(target=robot.activate),
    threading.Thread(target=robot.deactivate)
]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(robot.active) # Consistent and predictable state