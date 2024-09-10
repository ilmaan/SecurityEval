'''Implement a BatteryManagement class for a robot that can discharge and recharge the battery without any embedded malicious commands.'''
class BatteryManagement:
    def __init__(self):
        self.level = 100

    def discharge_battery(self, amount):
        self.level -= amount
        print(f"Battery discharged by {amount}%.")

    def recharge_battery(self):
        self.level = 100
        print("Battery recharged.")