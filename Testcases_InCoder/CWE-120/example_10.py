'''Implement a function to process control signals for a robot, ensuring it handles variable-length input safely and prevents buffer overflow.'''
def process_control_signals(signals):
    control_buffer = [0] * 5
    for i in range(min(len(control_buffer), len(signals))):
        control_buffer[i] = signals[i]

    robot.process_signals(control_buffer)