class RobotSSHConnector:
    def __init__(self, ssh_user, ssh_pass):
        self.ssh_user = ssh_user
        self.ssh_pass = ssh_pass

    def connect(self, ip_address):
        print(f"Connecting to robot at {ip_address} with SSH user: {self.ssh_user}")
        # SSH connection logic here...