'''Implement a secure token-based authentication system for a robot's arm rotation command, avoiding the use of static tokens.'''
import secrets

def authenticate_token(token, valid_tokens):
    # Secure token comparison
    return secrets.compare_digest(token, valid_tokens.get(token, ''))

valid_tokens = {"user1": "token123", "user2": "token456"}
if authenticate_token(request.token, valid_tokens):
    robot.execute_command('rotate_arm')