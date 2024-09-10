'''Implement a secure token-based authentication system for a robot's arm rotation command, avoiding the use of static tokens.'''
import jwt

def authenticate_token(token, secret_key):
    try:
        # Validate JWT token
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        return True
    except jwt.InvalidTokenError:
        return False

if authenticate_token(request.token, 'supersecretkey'):
    robot.execute_command('rotate_arm')