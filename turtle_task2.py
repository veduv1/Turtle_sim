#!usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist


def circle(radius):
    rospy.init_node('rotate')
    rospy.loginfo('Node has been started')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    cmd = Twist()
    for i in range(0, 10):
        cmd.linear.x = radius
        cmd.linear.y = 1.0
        cmd.angular.z = 2.0
        rospy.loginfo('radius is=%f', radius)
        pub.publish(cmd)
        rate.sleep()

if __name__ == '__main__':
    for j in range(1, 4):
        circle(j)
