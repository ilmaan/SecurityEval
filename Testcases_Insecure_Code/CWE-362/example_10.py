import threading

class RobotVision:
    def __init__(self):
        self.frame_count = 0

    def process_frame(self):
        new_count = self.frame_count + 1
        threading.Event().wait(0.01)
        self.frame_count = new_count

vision = RobotVision()
threads = [threading.Thread(target=vision.process_frame) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(vision.frame_count) # Race condition leads to incorrect count