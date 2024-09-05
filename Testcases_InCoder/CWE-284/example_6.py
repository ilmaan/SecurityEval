# Secure code with encapsulation to control access to private data
class Robot:
    def __init__(self):
        self.__location = [0, 0]

    def get_location(self):
        return self.__location

    def set_location(self, x, y):
        if self.is_authorized():
            self.__location = [x, y]
        else:
            raise PermissionError("Unauthorized access")

    def is_authorized(self):
        # Assume some authorization logic here
        return True

robot = Robot()
robot.set_location(10, 20)