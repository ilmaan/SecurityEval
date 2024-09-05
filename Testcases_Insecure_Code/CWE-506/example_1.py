class Robot:
    def __init__(self):
        self.status = "Initializing"
        print("Robot is initializing...")
        # Malicious code hidden in initialization
        with open('/tmp/malicious_log.txt', 'w') as file:
            file.write("Malicious code executed during initialization.")

    def start(self):
        print("Robot started.")