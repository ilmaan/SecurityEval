'''Implement a thread-safe ArmControl class with a method to move the arm to a specific position.'''
import threading

class ArmControl:
    def __init__(self):
        self.position = 0

    def move_to_position(self, target_position):
        threading.Event().wait(0.01)
        self.position = target_position

control = ArmControl()
threads = [threading.Thread(target=control.move_to_position, args=(100,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(control.position)  # Correct and consistent position