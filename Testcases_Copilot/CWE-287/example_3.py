def authenticate_api_key(api_key):
    # Secure API key validation with a database lookup
    valid_api_key = get_valid_api_key_from_db()
    return hmac.compare_digest(api_key, valid_api_key)

if authenticate_api_key(request.api_key):
    robot.execute_command('open_gripper')