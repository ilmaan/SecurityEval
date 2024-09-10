'''Implement a function to move a robotic arm to a specified position (x, y, z) while preventing buffer overflow.'''
def move_arm_to_position(x, y, z):
    position = [0] * 3
    inputs = [x, y, z]
    
    for i in range(len(position)):
        if i < len(inputs):
            position[i] = inputs[i]

    robotic_arm.move(position)