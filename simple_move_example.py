#!/usr/bin/env python3

import sys  # Add this line to import the sys module
import rospy
import moveit_commander
from moveit_commander import PlanningSceneInterface
from moveit_commander import MoveGroupCommander

def main():
    rospy.init_node('moveit_example', anonymous=True)

    # Initialize MoveIt commander
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = PlanningSceneInterface()
    group_name = "arm"
    move_group = MoveGroupCommander(group_name)

    # Plan to a joint position
    joint_goal = move_group.get_current_joint_values()
    joint_goal[0] = 0.5  # Adjust the joint position as needed
    move_group.go(joint_goal, wait=True)
    move_group.stop()

    # Shutdown MoveIt commander
    moveit_commander.roscpp_shutdown()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
