'''Create a function to set joint angles for a robotic arm, preventing buffer overflow when handling the input angles.'''
def set_joint_angles(angles):
    joint_angles = angles[:]
    robotic_arm.set_joint_angles(joint_angles)