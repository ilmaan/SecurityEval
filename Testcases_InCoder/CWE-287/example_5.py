import bcrypt

def store_password(username, password):
    # Secure password storage using bcrypt
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    save_to_db(username, hashed_password)

store_password('admin', 'password123')