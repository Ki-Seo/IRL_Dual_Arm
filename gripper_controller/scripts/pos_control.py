#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
import math

#import time
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from gripper_controller.msg import Inputpos
#from robot_mapping.msg import Serialmsg, Slavepos

class pos:
    def __init__(self):
        rospy.init_node('pos_control')
        position_sub = rospy.Subscriber("/input_command", Inputpos, self.callback_1, queue_size= 100)
        joint_sub = rospy.Subscriber("/joint_states", JointState, self.callback_2, queue_size= 100)

        self.pub_1 = rospy.Publisher('/second_controller/command', Float64, queue_size=10)
        self.pub_2 = rospy.Publisher('/third_controller/command', Float64, queue_size=10)
        self.pub_3 = rospy.Publisher('/first_controller/command', Float64, queue_size=10)
        
        self.flag = 0
        
    def callback_1(self, msg):
        self.command_1 = msg
        #print(self.command)
        self.flag = 1
    
    def callback_2(self, msg):
        self.position = msg.position
        self.flag = 2
        
    def talker(self):
        while not rospy.is_shutdown():
            if self.flag == 1: 
                self.pub_1.publish(self.command_1.pos_1)
                self.pub_2.publish(self.command_1.pos_2)
                self.pub_3.publish(self.command_1.pos_3)
                    
                print("publish done")
                self.flag = 0
            
            elif self.flag == 2 :
                self.pub_1.publish((self.position[5])+2.9)
                self.pub_2.publish(5.9-((self.position[7])+2.52))
                self.pub_3.publish(6.4-((self.position[9])+2.9))
                
                print("publish done")
                self.flag = 0
                
if __name__ == '__main__':
    try:
        main = pos()
        main.talker()
    except rospy.ROSInterruptException: pass

    
