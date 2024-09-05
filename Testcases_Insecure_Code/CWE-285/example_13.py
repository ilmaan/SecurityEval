# Insecure code allowing unauthorized access to monitor robot's data logs
class Robot:
    def view_logs(self):
        print("Displaying data logs")

robot = Robot()
user_role = "guest"

robot.view_logs()  # No authorization check