# IRL_Dual_Arm
#### 지능로봇 연구실 양팔로봇 제어 패키지
- gripper_controller : 그리퍼 제어 패키지
- irl_dual_arm : 양팔로봇 제어 패키지 (시뮬레이션)
- EtherCAT master(추가예정) : 통신 마스터 노드

## 설치
- 패키지 복사
<pre><code>$ cd /home/catkin_ws  #your ROS workspace</code></pre>
<pre><code>$ git clone https://github.com/Ki-Seo/IRL_Dual_Arm.git </code></pre>
---------------



## 실행
#### RVIZ 시뮬레이션 
- urdf file 실행
<pre><code>$ roslaunch irl_dual_arm irl_dual_arm.launch</code></pre>
- rviz 실행
<pre><code>$ rosrun rviz rviz</code></pre>


#### 그리퍼 위치제어
<<<<<<< Updated upstream
- 다이나믹셀 제어 노드 실행 
참고 사이트 : http://wiki.ros.org/dynamixel_controllers/Tutorials/CreatingJointPositionController, http://rosclub.cn/post-489.html 
  1개 제어 
    <pre><code>$ roscore</code></pre> 
    <pre><code>$ roslaunch dynamixel_tutorials controller_manager.launch</code></pre> 
    <pre><code>$ roslaunch dynamixel tutorials start_tilt_controller.launch</code></pre> 
    <pre><code>$ rostopic pub -1 /tilt_controller/command std_msgs/Float64 -- 1.5</code></pre> 
  다중 제어 
    <pre><code>$ roscore</code></pre> 
    <pre><code>$ roslaunch dynamixel_tutorials controller_manager.launch</code></pre> 
    <pre><code>$ roslaunch dynamixel tutorials start_(dual or triple)_controller.launch</code></pre> 
    <pre><code>$ rostopic pub -1 /(first or second or third)_controller/command std_msgs/Float64 -- 1.5</code></pre> 
=======
- 다이나믹셀 제어 노드 실행
참고 사이트 : http://wiki.ros.org/dynamixel_controllers/Tutorials/CreatingJointPositionController, http://rosclub.cn/post-489.html
	1개 제어
		<pre><code>$ roscore</code></pre>
		<pre><code>$ roslaunch dynamixel_tutorials controller_manager.launch</code></pre>
		<pre><code>$ roslaunch dynamixel tutorials start_tilt_controller.launch</code></pre>
		<pre><code>$ rostopic pub -1 /tilt_controller/command std_msgs/Float64 -- 1.5</code></pre>
	다중 제어
		<pre><code>$ roscore</code></pre>
		<pre><code>$ roslaunch dynamixel_tutorials controller_manager.launch</code></pre>
		<pre><code>$ roslaunch dynamixel tutorials start_(dual or triple)_controller.launch</code></pre>
		<pre><code>$ rostopic pub -1 /(first or second or third)_controller/command std_msgs/Float64 -- 1.5</code></pre>
>>>>>>> Stashed changes
- 그리퍼 제어 노드 실행
<pre><code>$ roscore</code></pre>
<pre><code>$ rosrun gripper_controller pos_control.py</code></pre>


- 모터 각도값 퍼블리시
<pre><code>$ rostopic pub -1 /input_command gripper_controller/Inputpos '{pos_1 : 30, pos_2 : 60, pos_3 : 90}'</code></pre>
-------

### 가제보 시뮬레이션
<pre><code>$ roscore</code></pre> 
<pre><code>$ roslaunch seven_dof_arm_gazebo irl_dual_arm_gazebo_control.launch</code></pre> 

