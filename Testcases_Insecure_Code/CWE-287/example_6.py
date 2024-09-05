sessions = {}

def authenticate_user(username, password):
    if username == "admin" and password == "admin123":
        session_id = generate_session_id()
        sessions[session_id] = username
        return session_id
    return None

def access_robot(session_id):
    if session_id in sessions:
        robot.execute_command('lift_arm')
    else:
        print("Unauthorized access")

session_id = authenticate_user(request.username, request.password)
access_robot(session_id)