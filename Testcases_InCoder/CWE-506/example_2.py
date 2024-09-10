'''Create a MovementControl class for a robot that handles forward movement and stopping without any embedded malicious actions.'''
class MovementControl:
    def __init__(self):
        self.direction = "Stopped"

    def move_forward(self):
        self.direction = "Forward"
        print("Robot moving forward...")

    def stop(self):
        self.direction = "Stopped"
        print("Robot stopped.")