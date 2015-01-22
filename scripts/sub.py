#!/usr/bin/env python
# This is a simple test harness to receive headers and compare
# sequence numbers and time stamps.

import rospy
from std_msgs.msg import Header

# the last sequence number received. -1 indicates nothing received yet
last_seq = -1

def format_time_str(time):
    """Helper function to make a pretty version of a time value in seconds"""
    return str(time.secs) + "." + "{:0>9d}".format(time.nsecs)

def callback(data):
    global last_seq
    # check that we haven't missed any messages
    if last_seq > 0 and data.seq != last_seq + 1:
        rospy.logerror("Sequence number mismatch: expected " + str(last_seq + 1)
            + " got " + data.seq)
    last_seq = data.seq

    # compare time stamps and print out
    rospy.loginfo("Received message with time " + format_time_str(data.stamp) + 
        ", delta " + format_time_str(rospy.Time.now() - data.stamp) + 
        ", message: " + str(data.frame_id))
    
def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("test", Header, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()