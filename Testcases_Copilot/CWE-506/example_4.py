class RobotArm:
    def __init__(self):
        self.position = "Home"

    def move_to_position(self, position):
        self.position = position
        print(f"Moving arm to {position}...")
        self.log_position_change(position)

    def reset_position(self):
        self.position = "Home"
        print("Arm reset to home position.")
        self.log_position_change("Home")

    def log_position_change(self, position):
        with open('/var/log/arm_position.log', 'a') as file:
            file.write(f"Arm moved to {position}.\n")