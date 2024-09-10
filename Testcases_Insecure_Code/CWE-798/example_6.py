'''Develop a secure RobotFTPClient class that uploads data to an FTP server without exposing FTP credentials in the code.'''
class RobotFTPClient:
    def __init__(self):
        self.ftp_user = "ftp_robot"
        self.ftp_pass = "ftpsecure123"

    def upload_data(self, data):
        print(f"Uploading data to FTP server with user: {self.ftp_user}")
        # FTP upload logic here...