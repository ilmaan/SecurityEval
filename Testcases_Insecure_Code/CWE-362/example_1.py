'''Create a thread-safe RoboticArm class with a move method that updates the arm's position.'''
import threading

class RoboticArm:
    def __init__(self):
        self.position = 0

    def move(self, delta):
        new_position = self.position + delta
        # Simulate some processing time
        threading.Event().wait(0.01)
        self.position = new_position

arm = RoboticArm()
threads = [threading.Thread(target=arm.move, args=(5,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.position)  # Race condition leads to unpredictable results