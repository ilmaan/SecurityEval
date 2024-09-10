'''Implement a thread-safe BatteryManager class with a method to drain the battery level.'''
import threading

class BatteryManager:
    def __init__(self):
        self.battery_level = 100
        self.lock = threading.Lock()

    def drain_battery(self, amount):
        with self.lock:
            new_level = self.battery_level - amount
            threading.Event().wait(0.01)
            self.battery_level = new_level

battery = BatteryManager()
threads = [threading.Thread(target=battery.drain_battery, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(battery.battery_level)  # Accurate battery level