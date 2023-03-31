#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from trajectory_msgs.msg import JointTrajectory
from tf.transformations import euler_from_quaternion

class myRobot():

    def __init__(self):
        print('init')
self.cmd_vel_twist = Twist()
self.tiago_odom = Odometry()
self.orientacao = 0.0

# Subscriber odometria
self.odom_sub = rospy.Subscriber('/mobile_base_controller/odom', Odometry, self.callback_odometria)

# Subscriber laser
self.laser_sub = rospy.Subscriber('/scan_raw', LaserScan, self.callback_laser, queue_size=1) #queue_size não é obrigatório

# Client Service camera

# Publisher base
self.base_pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)

# Publisher cabeca
self.head_pub = rospy.Publisher('/head_controller/command', JointTrajectory)

def callback_odometria(self, msg):
    print('callback odometria')
self.tiago_odom = msg.pose.pose.orientation
self.orientacao = euler_from_quaternion([self.tiago_odom.x, self.tiago_odom.y, self.tiago_odom.z, self.tiago_odom.w])[2] # posicao angular, em radianos, em torno do eixo z
# Armazenar os dados de odometria

def callback_laser(self, msg):
    print('callback laser')
#print(len(msg.ranges)) #retornou 666

#indice 333 (feixe a frente), 50 a 100 (esquerda) e 500 a 600 (direita)
if (msg.ranges[333] < 1):
    self.cmd_vel_twist.linear.x = 0
else:
    self.cmd_vel_twist.linear.x = msg.ranges[333] * 0.25

# Armazenar os dados do laser

def moveStraight(self):
#print('move straight')
#self.base_pub.publish(self.cmd_vel_twist)
    while self.orientacao < 1.57:
        self.cmd_vel_twist.angular.z = 0.1 #girar para esquerda; se for para direita é -0.1
        self.base_pub.publish(self.cmd_vel_twist)
# error = ...
# while(abs(error) < value):

def turn(self, sens):
    print('turn')
# error = ...
# while(abs(error) < value):

def decision(self):
    print('decision')

if __name__ == '__main__':

    rospy.init_node('project_tiago')

tiago = myRobot()

while not rospy.is_shutdown():
    tiago.moveStraight()

state = 0
# rospy.spin()
# while(...):
# if state == 0:
# decision
# compute next state
# else if state == 1
# image porcessing
# compute next state
# else if state == 3
# move straight
# compute next state
# else if state == 4
# turn
# compute next state
