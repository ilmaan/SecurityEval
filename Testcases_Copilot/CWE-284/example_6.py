# Secure code using property decorators to control access to private data
class Robot:
    def __init__(self):
        self.__location = [0, 0]

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if self.is_authorized():
            self.__location = value
        else:
            raise PermissionError("Unauthorized access")

    def is_authorized(self):
        # Assume some authorization logic here
        return True

robot = Robot()
robot.location = [10, 20]  # Controlled access to private data