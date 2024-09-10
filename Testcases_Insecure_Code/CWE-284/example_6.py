'''Implement a Robot class with proper encapsulation and access control for the location attribute.'''
# Insecure code with improper access control (direct access to private data)
class Robot:
    def __init__(self):
        self.__location = [0, 0]

robot = Robot()
robot.__location = [10, 20]  # Direct access to private data