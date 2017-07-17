#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
import math

#import time
from std_msgs.msg import Float64
from sensor_msgs.msg import JointState
from seven_dof_arm_gazebo.msg import Inputpos
#from robot_mapping.msg import Serialmsg, Slavepos

class pos:
    def __init__(self):
        rospy.init_node('irl_dual_arm_pos')
        position_sub = rospy.Subscriber("/input_command", Inputpos, self.callback_1, queue_size= 100)
        joint_sub = rospy.Subscriber("/joint_states", JointState, self.callback_2, queue_size= 100)

        self.pub_1 = rospy.Publisher('/irl_dual_arm/joint1_position_controller/command', Float64)
        self.pub_2 = rospy.Publisher('/irl_dual_arm/joint2_position_controller/command', Float64)
        self.pub_3 = rospy.Publisher('/irl_dual_arm/joint3_position_controller/command', Float64)
        self.pub_4 = rospy.Publisher('/irl_dual_arm/joint4_position_controller/command', Float64)
        self.pub_5 = rospy.Publisher('/irl_dual_arm/joint5_position_controller/command', Float64)
        self.pub_6 = rospy.Publisher('/irl_dual_arm/joint6_position_controller/command', Float64)
        self.pub_7 = rospy.Publisher('/irl_dual_arm/joint7_position_controller/command', Float64)
        self.pub_8 = rospy.Publisher('/irl_dual_arm/joint8_position_controller/command', Float64)
        self.pub_9 = rospy.Publisher('/irl_dual_arm/joint9_position_controller/command', Float64)
        self.pub_10 = rospy.Publisher('/irl_dual_arm/joint10_position_controller/command', Float64)
        self.pub_11 = rospy.Publisher('/irl_dual_arm/joint11_position_controller/command', Float64)
        
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
                self.pub_4.publish(self.command_1.pos_4)
                self.pub_5.publish(self.command_1.pos_5)
                self.pub_6.publish(self.command_1.pos_6)
                self.pub_7.publish(self.command_1.pos_7)
                self.pub_8.publish(self.command_1.pos_8)
                self.pub_9.publish(self.command_1.pos_9)
                self.pub_10.publish(self.command_1.pos_10)
                self.pub_11.publish(self.command_1.pos_11)
                    
                print("publish done")
                self.flag = 0
            
            elif self.flag == 2 :
                self.pub_1.publish(self.position[0])
                self.pub_2.publish(self.position[1])
                self.pub_3.publish(self.position[2])
                self.pub_4.publish(self.position[3])
                self.pub_5.publish(self.position[4])
                self.pub_6.publish(self.position[5])
                self.pub_7.publish(self.position[6])
                self.pub_8.publish(self.position[7])
                self.pub_9.publish(self.position[8])
                self.pub_10.publish(self.position[9])
                self.pub_11.publish(self.position[10])
                
                print("publish done")
                self.flag = 0
                
if __name__ == '__main__':
    try:
        main = pos()
        main.talker()
    except rospy.ROSInterruptException: pass

    
