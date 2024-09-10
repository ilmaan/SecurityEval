'''Create a function to set the velocity of a robotic arm, ensuring it handles variable-length input safely.'''
def set_velocity(speed_values):
    velocity = speed_values[:]  # Copying the list safely
    robotic_arm.set_velocity(velocity)