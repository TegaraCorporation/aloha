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
    robot_model = "wx250"
    bot = InterbotixManipulatorXS(robot_model, "arm", "gripper")

    if (bot.arm.group_info.num_joints < 5):
        print('This demo requires the robot to have at least 5 joints!')
        sys.exit()

    # Initial position
    bot.arm.set_ee_pose_components(x=0.3, z=0.2)
    bot.arm.set_single_joint_position("waist", np.pi / 2.0)
    bot.gripper.open()

    # Move left to pick (assume x=0.2 is to the left)
    bot.arm.set_ee_cartesian_trajectory(x=0.2)
    bot.gripper.close()

    # Move right after picking (assume x=-0.2 is to the right)
    bot.arm.set_ee_cartesian_trajectory(x=-0.2)
    bot.arm.set_single_joint_position("waist", -np.pi / 2.0)

    # Move left to place
    bot.arm.set_ee_cartesian_trajectory(x=0.2)
    bot.gripper.open()

    # Move right after placing
    bot.arm.set_ee_cartesian_trajectory(x=-0.2)

    # Return to home and then sleep pose
    bot.arm.go_to_home_pose()
    bot.arm.go_to_sleep_pose()

if __name__ == '__main__':
    main()
