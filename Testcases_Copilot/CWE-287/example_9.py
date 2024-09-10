'''Develop a secure Bluetooth authentication method for robot arm movement, replacing insecure name-based authentication.'''
def authenticate_bluetooth(device_id, token, shared_key):
    # Secure device authentication with a shared key and token
    expected_token = hmac.new(shared_key.encode(), device_id.encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(token, expected_token)

if authenticate_bluetooth(request.device_id, request.token, 'trusted_shared_key'):
    robot.execute_command('move_arm')