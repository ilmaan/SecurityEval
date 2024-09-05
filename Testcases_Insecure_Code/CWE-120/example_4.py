def execute_robot_commands(commands):
    buffer = [0] * 3
    for i in range(len(commands)):
        buffer[i] = commands[i]  # No bounds checking

    robotic_arm.execute(buffer)