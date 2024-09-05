def execute_robot_commands(commands):
    buffer = [0] * 3
    for i in range(min(len(buffer), len(commands))):
        buffer[i] = commands[i]

    robotic_arm.execute(buffer)