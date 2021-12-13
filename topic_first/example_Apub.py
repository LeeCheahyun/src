#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

# Bsub 받기 --------------------------
def fun_callback(msg):
    rospy.loginfo('%s',msg.data)
    return
# ------------------------------------

if __name__ == '__main__':
    rospy.init_node('sampleA_pub')
    pub = rospy.Publisher('helloA', String, queue_size=10)

    # Bsub 받기 ---------------------------
    rospy.Subscriber('hello03', String, callback=fun_callback)
    # -------------------------------------
    
    rate = rospy.Rate(10) 
    while not rospy.is_shutdown():
        str = "hello_publisher : %s " % rospy.get_time()
        pub.publish(str)
        rate.sleep()

    pass