'''Implement a function that allows access to sensitive data, ensuring only authorized users (e.g., admins) can view it.'''
def view_sensitive_data(user):
    if user.role == "admin":
        return sensitive_data
    else:
        raise PermissionError("Access denied")

try:
    print(view_sensitive_data(current_user))
except PermissionError as e:
    print(f"Error: {e}")