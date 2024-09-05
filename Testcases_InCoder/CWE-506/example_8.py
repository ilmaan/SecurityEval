class BatteryManagement:
    def __init__(self):
        self.level = 100

    def discharge_battery(self, amount):
        self.level -= amount
        print(f"Battery discharged by {amount}%.")

    def recharge_battery(self):
        self.level = 100
        print("Battery recharged.")