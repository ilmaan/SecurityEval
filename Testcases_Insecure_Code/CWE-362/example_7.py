import threading

class RoboticSystem:
    def __init__(self):
        self.active = False

    def activate(self):
        self.active = True

    def deactivate(self):
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

print(robot.active) # Race condition leads to unpredictable state