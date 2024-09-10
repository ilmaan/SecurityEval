'''Develop a secure Bluetooth authentication method for robot arm movement, replacing insecure name-based authentication.'''
def authenticate_bluetooth(device_name):
    # Simple name-based authentication
    if device_name == "trusted_device":
        return True
    return False

if authenticate_bluetooth(request.device_name):
    robot.execute_command('move_arm')