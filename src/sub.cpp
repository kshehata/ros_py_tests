#include "ros/ros.h"
#include "std_msgs/Header.h"

#include <sstream>

using namespace std;

void callback(const std_msgs::Header::ConstPtr& data)
{
  static int last_seq = -1;

  if ((last_seq > 0) && (data->seq != last_seq + 1))
  {
    ROS_ERROR("Sequence number mismatch: expected %d got %d", last_seq + 1, data->seq);
  }
  last_seq = data->seq;

  stringstream ss;
  ss << "CPP Received message with time " << data->stamp << ", delta " << 
    (ros::Time::now() - data->stamp) << ", message: " + data->frame_id;

  ROS_INFO("%s", ss.str().c_str());
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "listener");
  ros::NodeHandle n;
  ros::Subscriber sub = n.subscribe("test", 1000, callback);
  ros::spin();

  return 0;
}