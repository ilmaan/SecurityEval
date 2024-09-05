def set_velocity(speed_values):
    velocity = speed_values[:]  # Copying the list safely
    robotic_arm.set_velocity(velocity)