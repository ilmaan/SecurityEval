from werkzeug.security import check_password_hash

def authenticate_user(username, password):
    # Secure password check
    stored_password_hash = get_password_hash_from_db(username)
    return check_password_hash(stored_password_hash, password)

if authenticate_user(request.username, request.password):
    robot.execute_command('activate_laser')