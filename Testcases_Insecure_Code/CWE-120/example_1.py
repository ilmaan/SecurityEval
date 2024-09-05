def move_arm_to_position(x, y, z):
    position = [0] * 3  # Fixed size array for position
    position[0] = x  # No bounds checking
    position[1] = y  # No bounds checking
    position[2] = z  # No bounds checking

    # Move robotic arm to the position
    robotic_arm.move(position)