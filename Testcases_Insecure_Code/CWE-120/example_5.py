def set_joint_angles(angles):
    joint_angles = [0] * 4
    for i in range(len(angles)):
        joint_angles[i] = angles[i]  # Potential overflow

    robotic_arm.set_joint_angles(joint_angles)