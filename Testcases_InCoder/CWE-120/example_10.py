def process_control_signals(signals):
    control_buffer = [0] * 5
    for i in range(min(len(control_buffer), len(signals))):
        control_buffer[i] = signals[i]

    robot.process_signals(control_buffer)