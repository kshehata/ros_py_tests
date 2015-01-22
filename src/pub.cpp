#include "ros/ros.h"
#include "std_msgs/Header.h"

#include <sstream>

using namespace std;

/**
 * Simple test harness to send headers at 100 Hz.
 * Use time stamps and sequence numbers to check sync lost messages.
 */
int main(int argc, char **argv)
{
  ros::init(argc, argv, "publisher");
  ros::NodeHandle n;
  ros::Publisher pub = n.advertise<std_msgs::Header>("test", 1000);

  ros::Rate loop_rate(100);
  std_msgs::Header msg;

  while (ros::ok())
  {
    msg.stamp = ros::Time::now();
    std::stringstream ss;
    ss << "cpp hello world " << msg.stamp;
    msg.frame_id = ss.str();

    ROS_INFO("%s", msg.frame_id.c_str());

    pub.publish(msg);
    ros::spinOnce();

    loop_rate.sleep();
  }

  return 0;
}