class RobotArm:
    def __init__(self):
        self.position = "Home"

    def move_to_position(self, position):
        self.position = position
        print(f"Moving arm to {position}...")

    def reset_position(self):
        self.position = "Home"
        print("Arm reset to home position.")