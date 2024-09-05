import threading

class RoboticSystem:
    def __init__(self):
        self.active = False

    def activate(self):
        threading.Event().wait(0.01)
        threading.atomic_exchange(self, 'active', True)

    def deactivate(self):
        threading.Event().wait(0.01)
        threading.atomic_exchange(self, 'active', False)

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