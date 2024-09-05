def process_control_signals(signals):
    control_buffer = [0] * 5
    for i in range(len(signals)):
        control_buffer[i] = signals[i]  # No bounds checking

    robot.process_signals(control_buffer)