# ros_py_tests
Test harness for testing what happens when a rospy publisher broadcasts messages to multiple clients at a high rate. On some machines this works perfectly. On other machines, the sending rate drops quickly. To verify:

1. Launch the publisher and subscribers with roslaunch ros_py_tests py-py-test.launch
2. rostopic hz /test

If the message rate stays at 100 Hz then your machine is one of the lucky ones. If it drops significantly below 100 Hz, then you're witnessing the problem case.
