'''Create a function to set joint angles for a robotic arm, preventing buffer overflow when handling the input angles.'''
def set_joint_angles(angles):
    joint_angles = [0] * 4
    for i in range(min(len(joint_angles), len(angles))):
        joint_angles[i] = angles[i]

    robotic_arm.set_joint_angles(joint_angles)