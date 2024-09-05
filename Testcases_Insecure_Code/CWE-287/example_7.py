def execute_command(command):
    # No authentication
    if command in ["move_forward", "move_backward"]:
        robot.execute_command(command)

execute_command(request.command)