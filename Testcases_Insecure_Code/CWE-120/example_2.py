'''Create a function to set the velocity of a robotic arm, ensuring it handles variable-length input safely.'''
def set_velocity(speed_values):
    velocity = [0] * 4
    for i in range(len(speed_values)):
        velocity[i] = speed_values[i]  # Potential overflow

    robotic_arm.set_velocity(velocity)