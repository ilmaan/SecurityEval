def move_arm_to_position(x, y, z):
    position = [x, y, z]  # List can dynamically adjust size
    robotic_arm.move(position)