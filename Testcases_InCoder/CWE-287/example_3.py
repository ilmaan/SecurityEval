import hmac
import hashlib

def authenticate_api_key(api_key, secret_key):
    # HMAC for API key validation
    valid_key = hmac.new(secret_key.encode(), b'robot', hashlib.sha256).hexdigest()
    return hmac.compare_digest(api_key, valid_key)

if authenticate_api_key(request.api_key, 'supersecretkey'):
    robot.execute_command('open_gripper')