# IRL_Dual_Arm
#### 지능로봇 연구실 양팔로봇 제어 패키지
## 설치
- 패키지 복사
<pre><code>$ cd /home/catkin_ws  #your ROS workspace</code></pre>
<pre><code>$ cd git clone https://github.com/Ki-Seo/IRL_Dual_Arm.git </code></pre>
---------------
## 실행
#### RVIZ 시뮬레이션 
- urdf file 실행
<pre><code>$ roslaunch irl_dual_arm irl_dual_arm.launch</code></pre>
- rviz 실행
<pre><code>$ rosrun rviz rviz</code></pre>


#### 그리퍼 위치제어
- 그리퍼 제어 노드 실행
<pre><code>$ roscore</code></pre>
<pre><code>$ rosrun gripper_controller pos_control.py</code></pre>


- 모터 각도값 퍼블리시
<pre><code>$ rostopic pub -1 /input_command gripper_controller/Inputpos '{pos_1 : 30, pos_2 : 60, pos_3 : 90}'</code></pre>
-------
