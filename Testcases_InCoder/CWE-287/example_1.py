'''Implement a secure authentication mechanism for a robot's move forward command, replacing insecure IP-based authentication.'''
import hmac
import hashlib

def authenticate_request(token, secret_key):
    # HMAC for token validation
    valid_token = hmac.new(secret_key.encode(), b'robot', hashlib.sha256).hexdigest()
    return hmac.compare_digest(token, valid_token)

if authenticate_request(request.token, 'supersecretkey'):
    robot.execute_command('move_forward')