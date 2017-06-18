#!/usr/bin/env python
#-*- coding: utf-8 -*-
import rospy
import math

#import time
from std_msgs.msg import Float64
from gripper_controller.msg import Inputpos
#from robot_mapping.msg import Serialmsg, Slavepos

class pos:
    def __init__(self):
        rospy.init_node('gripper_pos')
        position_sub = rospy.Subscriber("/input_command", Inputpos, self.callback, queue_size= 100)
        

        self.pub_1 = rospy.Publisher('/first_controller/command', Float64, queue_size=10)
        self.pub_2 = rospy.Publisher('/second_controller/command', Float64, queue_size=10)
        self.pub_3 = rospy.Publisher('/third_controller/command', Float64, queue_size=10)
        
        self.flag = False
        
    def callback(self, msg):
        self.command = msg
        #print(self.command)
        self.flag = True
        
    def talker(self):
        while not rospy.is_shutdown():
            if self.flag == True: 
                self.pub_1.publish(math.radians(self.command.pos_1))
                self.pub_2.publish(math.radians(self.command.pos_2))
                self.pub_2.publish(math.radians(self.command.pos_3))
                    
                print("publish done")
                self.flag = False
                
            #self.r.sleep()
if __name__ == '__main__':
    try:
        main = pos()
        main.talker()
    except rospy.ROSInterruptException: pass

    