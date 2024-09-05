def authenticate_oauth(token):
    # Insecure OAuth token validation
    if token == "insecure_token":
        return True
    return False

if authenticate_oauth(request.token):
    robot.execute_command('start_drilling')