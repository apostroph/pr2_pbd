#!/usr/bin/env python

'''This runs the PbD system (i.e. the backend).'''

# Core ROS imports come first.
import rospy
import signal
from pr2_arm_control.arm import Arm
from pr2_arm_control.msg import Side
from pr2_arm_control.arm_control_marker import ArmControlMarker
from tf import TransformListener
from std_msgs.msg import String

class ArmControls:
    '''Marker for visualizing the steps of an action.'''

    def __init__(self):
    	tf_listener = TransformListener()
    	r_arm = Arm(Side.RIGHT, tf_listener)
    	l_arm = Arm(Side.LEFT, tf_listener)
    	self.r_marker = ArmControlMarker(r_arm)
    	self.l_marker = ArmControlMarker(l_arm)
        rospy.Subscriber('arm_control_reset', String, self.reset_arm_controls)
    	rospy.loginfo('Arm controls initialized.')

    def reset_arm_controls(self, dummy):
    	self.r_marker.reset()
    	self.l_marker.reset()
