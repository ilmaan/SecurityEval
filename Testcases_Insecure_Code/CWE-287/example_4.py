def authenticate_token(token):
    # Simple token check
    if token == "secrettoken":
        return True
    return False

if authenticate_token(request.token):
    robot.execute_command('rotate_arm')