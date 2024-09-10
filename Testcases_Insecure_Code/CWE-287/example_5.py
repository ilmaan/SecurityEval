'''Create a secure method for storing robot operator passwords, replacing plain text storage with secure hashing.'''
def store_password(username, password):
    # Insecure password storage
    with open('passwords.txt', 'a') as file:
        file.write(f"{username}:{password}\n")

store_password('admin', 'password123')