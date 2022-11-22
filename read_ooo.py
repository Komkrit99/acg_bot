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
        # hello_str = "hello world %s" % rospy.get_time()
pos = 'A3'
position = json.keys()
if pos in position:
    robot_move = pose()
    robot_move.position = pos
    robot_move.pose_x = float(json[pos][0])
    robot_move.pose_y = float(json[pos][1])
    robot_move.theta = float(json[pos][2])
    poo = float(json[pos][0])
    print(type(poo))
    print(poo)
        
# print(type(robot_move))

# robot_move.position = json['A1']
# robot_move.pose_x = json[pos][0]
# robot_move.pose_y = json['A1'][1]
# robot_move.theta = json['A1'][2]


# print(robot_move.pose_x)
# print(robot_move.pose_y)
# print(robot_move.theta)

# print(json['A1'][0])