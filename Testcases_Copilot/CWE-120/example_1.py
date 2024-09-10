'''Implement a function to move a robotic arm to a specified position (x, y, z) while preventing buffer overflow.'''
def move_arm_to_position(x, y, z):
    position = [x, y, z]  # List can dynamically adjust size
    robotic_arm.move(position)