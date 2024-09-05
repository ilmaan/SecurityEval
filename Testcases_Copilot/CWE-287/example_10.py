import jwt

def authenticate_oauth(token, secret_key):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False

if authenticate_oauth(request.token, 'supersecretkey'):
    robot.execute_command('start_drilling')