class RobotArm:
    def __init__(self):
        self.control_sequence = [10, 20, 30]

    def execute_sequence(self):
        print("Executing control sequence...")

    def shutdown(self):
        del self.control_sequence
        print("Control sequence freed.")

    def use_after_shutdown(self):
        self.shutdown()
        print(f"Continuing with control sequence: {self.control_sequence[0]}")  # Use after free