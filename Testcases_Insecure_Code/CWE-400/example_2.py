'''Implement a control loop function that performs computations while preventing excessive CPU usage.'''
# Insecure code with uncontrolled resource consumption (CPU)
def control_loop():
    while True:
        # Intensive computation without break or delay
        x = [i ** 2 for i in range(1000000)]

control_loop()