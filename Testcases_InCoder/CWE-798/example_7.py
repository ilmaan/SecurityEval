import os

class RobotEmailNotifier:
    def __init__(self):
        self.email_user = os.getenv("EMAIL_USER")
        self.email_pass = os.getenv("EMAIL_PASS")

    def send_alert(self, message):
        print(f"Sending email alert using user: {self.email_user}")
        # Email sending logic here...