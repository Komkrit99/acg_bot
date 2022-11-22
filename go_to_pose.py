#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from math import copysign
import math
from tf.transformations import euler_from_quaternion, quaternion_from_euler
#################### nav_go ###############################
# import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion
###########################################################

#################### VOICE ################################
from std_msgs.msg import Empty
###########################################################

#################### AGC04 Roller #########################
from std_msgs.msg import String
###########################################################
 
class GoToPose():
    
    def __init__(self, x, y, theta):

        self.goal_sent = False
    
        self.x_goal = x
        self.y_goal = y
        self.theta_goal = theta

        # What to do if shut down (e.g. Ctrl-C or failure)
        rospy.on_shutdown(self.shutdown)
	
	    # Tell the action client that we want to spin a thread by default
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo("Wait for the action server to come up")

	    # Allow up to 5 seconds for the action server to come up
        self.move_base.wait_for_server(rospy.Duration(5))

        self.goto()

    def goto(self):

        rospy.loginfo("Going to x:%f, " % self.x_goal + "y:%f, " % self.y_goal + "theta:%f, " % self.theta_goal)

        # Send a goal
        self.goal_sent = True
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = 'map'
        goal.target_pose.header.stamp = rospy.Time.now()

        goal.target_pose.pose.position.x = self.x_goal
        goal.target_pose.pose.position.y = self.y_goal
        goal.target_pose.pose.position.z = 0.0

        row = 0.0
        pitch = 0.0
        #theta -> rad
        yaw = math.radians(self.theta_goal)
        #rospy.loginfo("yaw [deg] = [%s]" % self.theta_goal)
        #rospy.loginfo("yaw [rad] = [%s]" % yaw)

        # Quaternion to Euler angles
        rot_q = goal.target_pose.pose.orientation
        (rot_q.x, rot_q.y, rot_q.z, rot_q.w) = quaternion_from_euler(row,pitch,yaw)
        #rospy.loginfo("qx = %s" % rot_q.x + "qy = %s" % rot_q.y + "qz = %s" % rot_q.z + "qw = %s" % rot_q.w)
        #rospy.loginfo("moving to x:%f, " % goal.x + "y:%f" % goal.y)

        goal.target_pose.pose.orientation.x = rot_q.x
        goal.target_pose.pose.orientation.y = rot_q.y
        goal.target_pose.pose.orientation.z = rot_q.z
        goal.target_pose.pose.orientation.w = rot_q.w

	    # Start moving
        self.move_base.send_goal(goal)

	    # Allow TurtleBot up to 60 seconds to complete task
        success = self.move_base.wait_for_result(rospy.Duration(300)) 

        state = self.move_base.get_state()
        result = False

        if success and state == GoalStatus.SUCCEEDED:
            # We made it!
            result = True
            rospy.loginfo("Hooray, reached the desired pose,")
            rospy.sleep(1)
        else:
            self.move_base.cancel_goal()
            rospy.loginfo("The base failed to reach the desired pose")
            rospy.sleep(1)

        self.goal_sent = False
        return result

    # def clear_costmaps_handler(self):
    #     rospy.loginfo("clear_costmaps_handler")

    def shutdown(self):
        if self.goal_sent:
            self.move_base.cancel_goal()
        rospy.loginfo("AGC04-GOTOPOSE is Stoped")
        rospy.sleep(1)