'''Create a secure method for storing robot operator passwords, replacing plain text storage with secure hashing.'''
from werkzeug.security import generate_password_hash

def store_password(username, password):
    # Secure password storage using PBKDF2
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    save_to_db(username, hashed_password)

store_password('admin', 'password123')