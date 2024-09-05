def set_joint_angles(angles):
    joint_angles = angles[:]
    robotic_arm.set_joint_angles(joint_angles)