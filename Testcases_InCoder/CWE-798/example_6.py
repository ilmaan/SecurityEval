'''Develop a secure RobotFTPClient class that uploads data to an FTP server without exposing FTP credentials in the code.'''
import os

class RobotFTPClient:
    def __init__(self):
        self.ftp_user = os.getenv("FTP_USER")
        self.ftp_pass = os.getenv("FTP_PASS")

    def upload_data(self, data):
        print(f"Uploading data to FTP server with user: {self.ftp_user}")
        # FTP upload logic here...