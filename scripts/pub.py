#!/usr/bin/env python
# Simple test harness to publish a header at 100 Hz
# populates time stamps and sequence numbers so clients can check for
# time sync and lost messages

import rospy
from std_msgs.msg import Header

def sender():
    pub = rospy.Publisher('test', Header, queue_size=10)
    rospy.init_node('sender', anonymous=True)
    rate = rospy.Rate(100)
    msg = Header()
    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        msg.frame_id = "python hello world %s" % msg.stamp
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        sender()
    except rospy.ROSInterruptException:
        pass
