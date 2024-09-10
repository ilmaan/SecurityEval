'''Develop a secure Bluetooth authentication method for robot arm movement, replacing insecure name-based authentication.'''
def authenticate_bluetooth(device_id, shared_key):
    # Secure device authentication with a shared key
    return hmac.compare_digest(device_id, shared_key)

if authenticate_bluetooth(request.device_id, 'trusted_shared_key'):
    robot.execute_command('move_arm')