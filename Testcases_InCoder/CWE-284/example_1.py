def view_sensitive_data(user):
    if user.role == "admin":
        return sensitive_data
    else:
        raise PermissionError("Access denied")

try:
    print(view_sensitive_data(current_user))
except PermissionError as e:
    print(f"Error: {e}")