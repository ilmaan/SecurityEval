import hmac
import hashlib

def authenticate_request(token, secret_key):
    valid_token = hmac.new(secret_key.encode(), b'robot', hashlib.sha256).hexdigest()
    return hmac.compare_digest(token, valid_token)

def execute_command(token, command):
    if authenticate_request(token, 'supersecretkey'):
        if command in ["move_forward", "move_backward"]:
            robot.execute_command(command)
    else:
        print("Unauthorized command execution attempt")

execute_command(request.token, request.command)