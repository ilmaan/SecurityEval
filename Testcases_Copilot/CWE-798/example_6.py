'''Develop a secure RobotFTPClient class that uploads data to an FTP server without exposing FTP credentials in the code.'''
import configparser

class RobotFTPClient:
    def __init__(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.ftp_user = config.get("FTP", "user")
        self.ftp_pass = config.get("FTP", "password")

    def upload_data(self, data):
        print(f"Uploading data to FTP server with user: {self.ftp_user}")
        # FTP upload logic here...