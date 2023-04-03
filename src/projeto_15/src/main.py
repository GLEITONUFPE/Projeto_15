#! /usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import euler_from_quaternion
from math import pi
from projeto_15.srv import Camera, CameraRequest

minimum_dist = 1.5

class myRobot():

    def __init__(self):
        #print('init')
        self.result = False
        self.rate = rospy.Rate(10)
        self.cmd_vel_twist = Twist()
        self.tiago_odom = Odometry()
        self.theta_z = 0.0
        self.mid_dist = 0.0
        self.left_dist = 0.0
        self.right_dist = 0.0
        # Subscriber odometria
        self.odom_sub = rospy.Subscriber('/mobile_base_controller/odom', Odometry, self.callback_odometria)
        # Subscriber laser
        self.laser_sub = rospy.Subscriber('/scan_raw', LaserScan, self.callback_laser, queue_size=1) #queue_size não é obrigatório
        # Client Service camera
        self.cam_srv = rospy.ServiceProxy('camera', Camera)

        # Publisher base
        self.base_pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=1)
        # Publisher cabeca
        self.head_pub = rospy.Publisher('/head_controller/command', JointTrajectory, queue_size=1)

        while self.theta_z == 0.0 or self.mid_dist == 0.0 or self.left_dist == 0.0 or self.right_dist == 0.0:
            pass

    def read_cam(self):
        rospy.wait_for_service('camera')
        try:
            request = CameraRequest()
            r = self.cam_srv(request)
            print(r.result)
            return r.result
        except rospy.ServiceException as e:
            print("Service call failed: %s"%e)       

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
        #pegar os indices 333 (frente), 22 (direita) e 643 (esquerda)
        self.mid_dist = msg.ranges[333]
        self.left_dist = msg.ranges[643]
        self.right_dist = msg.ranges[22]
    
    def moveHead(self):
        side = 0
        self.head_trajectory = JointTrajectory()
        self.head_trajectory.joint_names = ["head_1_joint", "head_2_joint"]
        self.head_trajectory.points = [JointTrajectoryPoint()]
        self.head_trajectory.points[0].positions = [0, 0]
        self.head_trajectory.points[0].time_from_start = rospy.Duration(0.1)
        self.head_pub.publish(self.head_trajectory)
        rospy.sleep(0.1)
        self.head_trajectory.points[0].positions = [-pi / 2, 0]
        self.head_trajectory.points[0].time_from_start = rospy.Duration(3.0)
        self.head_pub.publish(self.head_trajectory)
        #rospy.sleep(3)
        # direita
        if self.read_cam():
            side = 2
        rospy.sleep(3)
        if self.read_cam():
            side = 2
        rospy.sleep(3)
        self.head_trajectory.points[0].positions = [pi / 2, 0]
        self.head_trajectory.points[0].time_from_start = rospy.Duration(3.0)
        self.head_pub.publish(self.head_trajectory)
        #rospy.sleep(3)
        if self.read_cam():
            side = 1
        rospy.sleep(3)
        if self.read_cam():
            side = 1
        rospy.sleep(3)
        self.head_trajectory.points[0].positions = [0, 0]
        self.head_trajectory.points[0].time_from_start = rospy.Duration(3.0)
        self.head_pub.publish(self.head_trajectory)
        rospy.sleep(3)
        print(side)
        return side

    def moveStraight(self):
        #print('move straight')
        while (self.mid_dist > minimum_dist):
            #self.cmd_vel_twist.linear.x = self.mid_dist * 0.25
            self.cmd_vel_twist.linear.x = 1
            self.base_pub.publish(self.cmd_vel_twist)
        self.cmd_vel_twist.linear.x = 0
        d = self.mid_dist
        while (abs(d - self.mid_dist) > 0.05):
            d = self.mid_dist

    def turn_left(self):
        print('turn left')
        desired_theta = self.theta_z + (pi / 2)
        if desired_theta > pi:
            desired_theta -= 2 * pi
        while abs(desired_theta - self.theta_z) > 0.01:
            self.cmd_vel_twist.angular.z = 2 * abs(desired_theta - self.theta_z) #gira pra esquerda; pra direita, -0.1
            self.base_pub.publish(self.cmd_vel_twist)

    def turn_right(self):
        print('turn right')
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
        if self.mid_dist > minimum_dist:
            print("decision 1")
            self.moveStraight()
            return 1
        if self.left_dist > minimum_dist-0.2 and self.right_dist < minimum_dist-0.2:
            print("decision 2")
            self.turn_left()
            return 1
        if self.left_dist < minimum_dist and self.right_dist > minimum_dist:
            print("decision 3")
            self.turn_right()
            return 1
        if self.left_dist < minimum_dist and self.right_dist < minimum_dist:
            print("decision 4")
            self.moveStraight()
            return 1
        if self.left_dist > minimum_dist and self.right_dist > minimum_dist:
            print("decision 5")
            side = self.moveHead()
            if side == 1:
                self.turn_left()
                return 1
            elif side == 2:
                self.turn_right()
                return 1
            else:
                return 0

if __name__ == '__main__':

    rospy.init_node('project_tiago')
    
    tiago = myRobot()

    d = 1
    while not rospy.is_shutdown() and d == 1:
        d = tiago.decision()
        tiago.rate.sleep()
    #tiago.turn_right()
    # tiago.moveHead()


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