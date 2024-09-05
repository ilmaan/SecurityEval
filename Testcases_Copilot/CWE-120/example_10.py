def process_control_signals(signals):
    control_buffer = signals[:]
    robot.process_signals(control_buffer)