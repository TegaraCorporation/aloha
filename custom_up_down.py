from interbotix_xs_modules.arm import InterbotixManipulatorXS
import numpy as np
import sys

# This script makes the end-effector perform pick, pour, and place tasks
# Note that this script may not work for every arm as it was designed for the wx250
# Make sure to adjust commanded joint positions and poses as necessary
#
# To get started, open a terminal and type 'roslaunch interbotix_xsarm_control xsarm_control.launch robot_model:=wx250'
# Then change to this directory and type 'python bartender.py  # python3 bartender.py if using ROS Noetic'

def main():
    bot = InterbotixManipulatorXS("wx250", "arm", "gripper")

    if (bot.arm.group_info.num_joints < 5):
        print('This demo requires the robot to have at least 5 joints!')
        sys.exit()

    # Initial position
    bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    bot.arm.set_single_joint_position("waist", np.pi / 2.0)
    bot.gripper.open()

    # Move down to pick (ensure not going below ground level, assumed z=0.1 is above ground)
    bot.arm.set_ee_cartesian_trajectory(z=-0.1)
    bot.gripper.close()

    # Move up after picking
    bot.arm.set_ee_cartesian_trajectory(z=0.1)
    bot.arm.set_single_joint_position("waist", -np.pi / 2.0)

    # Pouring motion
    bot.arm.set_ee_cartesian_trajectory(pitch=1.5)
    bot.arm.set_ee_cartesian_trajectory(pitch=-1.5)
    bot.arm.set_single_joint_position("waist", np.pi / 2.0)

    # Move down to place (ensure not going below ground level)
    bot.arm.set_ee_carte
