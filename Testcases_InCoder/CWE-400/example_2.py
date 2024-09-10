'''Implement a control loop function that performs computations while preventing excessive CPU usage.'''
# Secure code with controlled resource consumption (CPU)
import time

def control_loop():
    while True:
        x = [i ** 2 for i in range(1000000)]
        time.sleep(0.1)  # Adding a delay to reduce CPU usage

control_loop()