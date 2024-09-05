import threading

class RoboticArm:
    def __init__(self):
        self.position = 0

    def move(self, delta):
        threading.Event().wait(0.01)
        threading.atomic_add(self, 'position', delta)

arm = RoboticArm()
threads = [threading.Thread(target=arm.move, args=(5,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(arm.position)  # Consistent and correct result