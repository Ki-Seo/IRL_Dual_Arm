# IRL_Dual_Arm
지능로봇 연구실 양팔로봇 제어 패키지


1. RVIZ 시뮬레이션
$ roslaunch irl_dual_arm irl_dual_arm.launch
$ rosrun rviz rviz


2. 그리퍼 위치제어
2.1 그리퍼 제 노드 실행
$ roscore
$ rosrun gripper_controller pos_control.py


2.2 모터 각도값 퍼블리시
$ rostopic pub -1 /input_command gripper_controller/Inputpos '{pos_1 : 30, pos_2 : 60, pos_3 : 90}'


