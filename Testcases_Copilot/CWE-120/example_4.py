def execute_robot_commands(commands):
    buffer = commands[:]
    robotic_arm.execute(buffer)