#!/usr/bin/env python
from logging import disable
from threading import current_thread
import rospy
from geometry_msgs.msg import Twist
pi=3.1415926535897

def move(distance):
    rospy.init_node('DNT_ROX',anonymous=True)
    v=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    temp=Twist()
    print("Moving robot")
    temp.linear.x=10
    temp.linear.y=0
    temp.linear.z=0
    temp.angular.x=0
    temp.angular.y=0
    temp.angular.z=0

    while not rospy.is_shutdown():
        time=rospy.Time.now().to_sec()
        cur_dist=0
        while(cur_dist<distance):
            v.publish(temp)
            time1=rospy.Time.now().to_sec()
            cur_dist=(time1-time)*10
        temp.linear.x=0
        v.publish(temp)
        break

def rotate(angle):
    v=rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    temp=Twist()
    print('rotating turtle')
    temp.linear.x=0
    temp.linear.y=0
    temp.linear.z=0
    temp.angular.x=0
    temp.angular.y=0
    temp.angular.z=200*pi/360
    
    curr_angle=0
    time=rospy.Time.now().to_sec()

    while(curr_angle<angle):
        print("hi")
        v.publish(temp)
        time1=rospy.Time.now().to_sec()
        curr_angle=100*(time1-time)
    temp.angular.z=0
    v.publish(temp)


move(5)
rotate(90)
print("done")