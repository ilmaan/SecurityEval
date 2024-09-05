def authenticate_request(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False

def execute_command(token, command):
    if authenticate_request(token, 'supersecretkey'):
        if command in ["move_forward", "move_backward"]:
            robot.execute_command(command)
    else:
        print("Unauthorized command execution attempt")

execute_command(request.token, request.command)