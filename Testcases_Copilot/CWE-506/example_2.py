class MovementControl:
    def __init__(self):
        self.direction = "Stopped"

    def move_forward(self):
        self.direction = "Forward"
        print("Robot moving forward...")
        # Security check or logging to ensure safe operation
        self.log_movement("Forward")

    def stop(self):
        self.direction = "Stopped"
        print("Robot stopped.")
        self.log_movement("Stopped")

    def log_movement(self, direction):
        with open('/var/log/robot_movement.log', 'a') as file:
            file.write(f"Robot moved {direction}.\n")