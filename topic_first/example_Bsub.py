#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

def fun_callback(msg):
    rospy.loginfo('%s',msg.data)

    # Apub한테 보내기 -----------------------------
    pub = rospy.Publisher('hello03', String, queue_size=10)
    pub.publish(msg.data)
    # --------------------------------------------
    return

if __name__ == '__main__':
    rospy.init_node('sample_Bsub')
    rospy.Subscriber('helloB', String, callback=fun_callback)
    rospy.Subscriber('helloB02', String, callback=fun_callback)
    rospy.spin()

    pass