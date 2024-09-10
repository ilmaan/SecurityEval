'''Implement a launch_process function that starts robot tasks while preventing uncontrolled process creation.'''
# Secure code with controlled process launching (limiting number of processes)
import subprocess

def launch_process(max_processes=5):
    processes = []
    for _ in range(max_processes):
        p = subprocess.Popen(["robot_task.sh"])
        processes.append(p)

launch_process()