import jwt

def authenticate_request(token, secret_key):
    try:
        # Decode JWT and validate signature
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.ExpiredSignatureError:
        print("Token expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")
    return False

if authenticate_request(request.token, 'supersecretkey'):
    robot.execute_command('move_forward')