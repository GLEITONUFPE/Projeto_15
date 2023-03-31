#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from trajectory_msgs.msg import JointTrajectory
from tf.transformations import euler_from_quaternion
from math import pi

class myRobot():

    def __init__(self):
        #print('init')
        self.cmd_vel_twist = Twist()
        self.tiago_odom = Odometry()
        self.theta_z = 0.0
        self.mid_dist = 0.0
        # Subscriber odometria
        self.odom_sub = rospy.Subscriber('/mobile_base_controller/odom', Odometry, self.callback_odometria)
        # Subscriber laser
        self.laser_sub = rospy.Subscriber('/scan_raw', LaserScan, self.callback_laser, queue_size=1) #queue_size não é obrigatório
        # Client Service camera
        # Publisher base
        self.base_pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)
        # Publisher cabeca
        self.head_pub = rospy.Publisher('/head_controller/command', JointTrajectory)

        while self.theta_z == 0.0:
            pass

    def callback_odometria(self, msg):
        #print('callback odometria')
        self.tiago_odom = msg.pose.pose.orientation
        self.theta_z = euler_from_quaternion([self.tiago_odom.x, self.tiago_odom.y, self.tiago_odom.z, self.tiago_odom.w])[2] # posicao angular, em radianos, em torno do eixo z
        # Armazenar os dados de odometria
        #print('self.theta_z = %f' %self.theta_z)

    def callback_laser(self, msg):
        #print('callback laser')
        #print(len(msg.ranges)) #retornou 666
        # movimentacao não pode estar em um callback, porque ele é executado o tempo todo
        #pegar os indices 333 (frente), 50 (direita) e 600 (esquerda)
        self.mid_dist = msg.ranges[333]


        # Armazenar os dados do laser

    def moveStraight(self):
        #print('move straight')
        if self.mid_dist < 1.00:
            self.cmd_vel_twist.linear.x = 0
        else:
            self.cmd_vel_twist.linear.x = self.mid_dist * 0.25
        self.base_pub.publish(self.cmd_vel_twist)

        # error = ...
        # while(abs(error) < value):

    def turn_left(self):
        desired_theta = self.theta_z + (pi / 2)
        if desired_theta > pi:
            desired_theta -= 2 * pi
        while abs(desired_theta - self.theta_z) > 0.01:
            self.cmd_vel_twist.angular.z = 2 * abs(desired_theta - self.theta_z) #gira pra esquerda; pra direita, -0.1
            self.base_pub.publish(self.cmd_vel_twist)

    def turn_right(self):
        desired_theta = self.theta_z - (pi / 2)
        if desired_theta < -pi:
            desired_theta += 2 * pi
        while abs(desired_theta - self.theta_z) > 0.01:
            self.cmd_vel_twist.angular.z = -2 * abs(desired_theta - self.theta_z) #gira pra direita
            self.base_pub.publish(self.cmd_vel_twist)
        # error = ...
        # while(abs(error) < value):

    def decision(self):
        print('decision')
        #

if __name__ == '__main__':

    rospy.init_node('project_tiago')
    
    rate = rospy.Rate(5)
    tiago = myRobot()
    rate.sleep()
    #while not rospy.is_shutdown():
        #tiago.moveStraight()
    tiago.turn_right()


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

#recomendações:
#setar publihsers e subscribers
#criar uma função para cada coisa (andar, rotacionar, detectar obstáculo, etc.)
#Para a próxima chamada, já ter passasdo dessa primeira fase.
#Esquecer processamento da imagem por enquanto.
#