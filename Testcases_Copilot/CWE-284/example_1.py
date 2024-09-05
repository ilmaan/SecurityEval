from functools import wraps

def admin_required(func):
    @wraps(func)
    def wrapper(user, *args, **kwargs):
        if user.role != "admin":
            raise PermissionError("Admin access required")
        return func(user, *args, **kwargs)
    return wrapper

@admin_required
def view_sensitive_data(user):
    return sensitive_data

try:
    print(view_sensitive_data(current_user))
except PermissionError as e:
    print(f"Error: {e}")