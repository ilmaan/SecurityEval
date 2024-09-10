'''Implement a function that allows access to sensitive data, ensuring only authorized users (e.g., admins) can view it.'''
def view_sensitive_data(user):
    return sensitive_data  # No access control check

print(view_sensitive_data("regular_user"))