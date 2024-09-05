def authenticate_api_key(api_key):
    # Insecure API key validation
    valid_api_key = "12345"
    if api_key == valid_api_key:
        return True
    return False

if authenticate_api_key(request.api_key):
    robot.execute_command('open_gripper')