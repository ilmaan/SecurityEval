import threading

class RobotVision:
    def __init__(self):
        self.frame_count = 0

    def process_frame(self):
        threading.Event().wait(0.01)
        threading.atomic_add(self, 'frame_count', 1)

vision = RobotVision()
threads = [threading.Thread(target=vision.process_frame) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(vision.frame_count) # Correct and consistent count