import threading

class BatteryManager:
    def __init__(self):
        self.battery_level = 100

    def drain_battery(self, amount):
        threading.Event().wait(0.01)
        self.battery_level -= amount

battery = BatteryManager()
threads = [threading.Thread(target=battery.drain_battery, args=(10,)) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(battery.battery_level)  # Accurate battery level