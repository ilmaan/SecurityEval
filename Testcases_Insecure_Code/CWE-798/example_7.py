class RobotEmailNotifier:
    def __init__(self):
        self.email_user = "robot_alerts"
        self.email_pass = "alertpass123"

    def send_alert(self, message):
        print(f"Sending email alert using user: {self.email_user}")
        # Email sending logic here...