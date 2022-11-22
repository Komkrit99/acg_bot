#!/usr/bin/env python
# license removed for brevity
import rospy
from agc_goto_pose.msg import pose  

f = open('/home/prem/test_robot_pose.txt', 'r')
#data = f.read()
data = f.read()
json = {}
loop = data.split('\n')
for i in loop:
# data = f.readline()
    data_tmp = i.replace(' ','').split('=')
    if(len(data_tmp) > 1):
        json[data_tmp[0]] = data_tmp[1].replace(' ','').replace(']','').replace('[','').split(',')
# print(json['A1'])
f.close()
pos = 'A3'
position = json.keys()
if pos in position:
    robot_move = pose()
    robot_move.position = pos
    robot_move.pose_x = float(json[pos][0])
    robot_move.pose_y = float(json[pos][1])
    robot_move.theta = float(json[pos][2])
def talker():
    message_pub = rospy.Publisher("Robot_pose", pose, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
            
            # rospy.loginfo(type(robot_move.pose_x))
            message_pub.publish(robot_move)
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass


# robot_move.position = json['A1']
# robot_move.pose_x = json[pos][0]
# robot_move.pose_y = json['A1'][1]
# robot_move.theta = json['A1'][2]

# print(robot_move.position)
# print(robot_move.pose_x)
# print(robot_move.pose_y)
# print(robot_move.theta)

# print(json['A1'][0])
