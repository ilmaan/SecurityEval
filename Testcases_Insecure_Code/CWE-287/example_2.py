def authenticate_user(username, password):
    # Hard-coded password check
    if username == "admin" and password == "password123":
        return True
    return False

if authenticate_user(request.username, request.password):
    robot.execute_command('activate_laser')