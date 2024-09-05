def view_sensitive_data(user):
    return sensitive_data  # No access control check

print(view_sensitive_data("regular_user"))