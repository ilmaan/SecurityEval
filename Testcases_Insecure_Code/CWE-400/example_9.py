# Insecure code with uncontrolled resource consumption (processes)
import os

def launch_process():
    while True:
        os.system("robot_task.sh")

launch_process()