import secrets

sessions = {}

def authenticate_user(username, password):
    if check_credentials(username, password):
        session_id = secrets.token_hex(32)
        sessions[session_id] = {'username': username, 'expires_at': time.time() + 1800}
        return session_id
    return None

def access_robot(session_id):
    session = sessions.get(session_id)
    if session and session['expires_at'] > time.time():
        robot.execute_command('lift_arm')
    else:
        print("Unauthorized access")

session_id = authenticate_user(request.username, request.password)
access_robot(session_id)