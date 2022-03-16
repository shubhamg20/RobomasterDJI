#!/usr/bin/env python
from roborts_msgs.srv import *
import rospy
rospy.wait_for_service('cmd_fric_wheel')
rospy.wait_for_service('cmd_shoot')
try:
    rospy.init_node('testing', anonymous=True)
    fric=rospy.ServiceProxy('cmd_fric_wheel',FricWhl)
    fric(0)
    shoot=rospy.ServiceProxy('cmd_shoot',ShootCmd)
    shoot(1,5)
except rospy.ServiceException as e:
    print(e)    
    