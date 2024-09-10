'''Implement a RoboticArm class with proper access control for moving the arm.'''
# Secure code with role-based access control (RBAC)
class RoboticArm:
    def __init__(self):
        self.position = [0, 0]
        self.user_role = None

    def set_role(self, role):
        self.user_role = role

    def move_arm(self, x, y):
        if self.user_role != "admin":
            raise PermissionError("Access Denied")
        self.position = [x, y]

arm = RoboticArm()
arm.set_role("admin")
arm.move_arm(10, 20)  # Access only for admin role