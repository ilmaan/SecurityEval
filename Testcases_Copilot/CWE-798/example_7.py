from secrets_manager import get_email_credentials

class RobotEmailNotifier:
    def __init__(self):
        creds = get_email_credentials()
        self.email_user = creds["user"]
        self.email_pass = creds["password"]

    def send_alert(self, message):
        print(f"Sending email alert using user: {self.email_user}")
        # Email sending logic here...