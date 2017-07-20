import rospy
from irl_dual_arm.srv import gripper_total_control

class gripper_total:
    def __init__(self):
        self.gripper_total_control_srv = rospy.service('gripper_total', gripper_total_control, self.gripper)
        self.pub_9 = rospy.Publisher('/irl_dual_arm/joint9_position_controller/command', Float64)
        self.pub_10 = rospy.Publisher('/irl_dual_arm/joint10_position_controller/command', Float64)
        self.pub_11 = rospy.Publisher('/irl_dual_arm/joint11_position_controller/command', Float64)
        print ("Ready to gripper_total_control.")
        
    def gripper(self, req):
        if req.flag = 1
            self.pub_9(1)
            self.pub_10(1)
            self.pub_11(1)
            req.flag = 0
        else if req.flag = 2
            self.pub_9(0)
            self.pub_10(0)
            self.pub_11(0)
            req.flag = 0
        else
            req.flag = 0
            
if __name__ == '__main__':
    try:
        main = gripper_total()
        rospy.spin()
    except rospy.ROSInterruptException: pass  