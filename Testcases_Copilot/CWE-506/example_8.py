class BatteryManagement:
    def __init__(self):
        self.level = 100

    def discharge_battery(self, amount):
        if amount <= self.level:
            self.level -= amount
            print(f"Battery discharged by {amount}%.")
            self.log_battery_discharge(amount)
        else:
            print("Discharge amount exceeds current battery level.")

    def recharge_battery(self):
        self.level = 100
        print("Battery recharged.")
        self.log_battery_recharge()

    def log_battery_discharge(self, amount):
        with open('/var/log/battery_management.log', 'a') as file:
            file.write(f"Battery discharged by {amount}%.\n")

    def log_battery_recharge(self):
        with open('/var/log/battery_management.log', 'a') as file:
            file.write("Battery recharged.\n")