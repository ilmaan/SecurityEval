'''Create a function to set the velocity of a robotic arm, ensuring it handles variable-length input safely.'''
def set_velocity(speed_values):
    velocity = [0] * 4
    for i in range(min(len(velocity), len(speed_values))):
        velocity[i] = speed_values[i]

    robotic_arm.set_velocity(velocity)