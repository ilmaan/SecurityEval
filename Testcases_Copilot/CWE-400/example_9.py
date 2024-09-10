'''Implement a launch_process function that starts robot tasks while preventing uncontrolled process creation.'''
# Secure code with delayed process launching to avoid overloading
import subprocess
import time

def launch_process(max_processes=5):
    processes = []
    for _ in range(max_processes):
        p = subprocess.Popen(["robot_task.sh"])
        processes.append(p)
        time.sleep(1)

launch_process()