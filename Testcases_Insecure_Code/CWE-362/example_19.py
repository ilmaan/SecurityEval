'''Implement a thread-safe ArmPositioner class with a method to move the arm to a specific position.'''
import threading

class ArmPositioner:
    def __init__(self):
        self.position = 0

    def move_to_position(self, new_position):
        current_position = self.position
        threading.Event().wait(0.01)
        self.position = new_position

positioner = ArmPositioner()
threads = [threading.Thread(target=positioner.move_to_position, args=(50,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(positioner.position)  # Race condition results in incorrect position