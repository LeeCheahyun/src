#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from rospy.core import is_shutdown


if __name__ == '__main__':
    rospy.init_node('simturtle_publisher')
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    twist = Twist()

    speed = 40
    angle = 180 #degree

    angular_speed = (speed*2*3.14)/360
    relative_angle = (angle*2*3.14)/360

    # angular_relative = 180
    # angular_speed = (angular_relative*3.14*2)/360

    # twist.angular.z = angular_speed
    # relative = angular_relative
    # relative = 3.14
    # current = 1

    time0 = rospy.Time.now().to_sec()
    current = 0
    twist.angular.z = angular_speed
    while current < relative_angle:
        pub.publish(twist)
        time1 = rospy.Time.now().to_sec()
        current = angular_speed * (time1-time0)

    twist.angular.z = 0.0
    pass