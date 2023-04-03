#! /usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
import numpy as np

from projeto_15.srv import Camera, CameraResponse

class myCamera():

    def __init__(self):
        print('init camera')
        # Bridge to convert ROS message to openCV
        self.bridge = CvBridge()
        
        # Row - Column
        self.row = 0
        self.col = 0

        # Subscriber to the camera image
        self.image_sub = rospy.Subscriber("/xtion/rgb/image_color",Image,self.imageCallBack)

        self.cam_serv = rospy.Service('camera', Camera, self.callback_ServiceCamera)

        self.result = False

    def callback_ServiceCamera(self, request):
        print('image service')
        self.res = CameraResponse()
        self.res = self.result
        return self.res

    def imageCallBack(self, msg):
        print('callback camera')
        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        except CvBridgeError as e:
            print(e)

        # Extract the image dimension
        self.row = msg.height # Number of rows/lines
        self.col = msg.width # Number of columns
        
        ##############################################################
        # Uncomment to resize the image and reduce the processing time
        ##############################################################
        
        # # New dimensions
        # ratio = 2
        # self.row /= ratio
        # self.col /= ratio
        # # Resize the image
        # self.cv_image = cv2.resize(self.cv_image,(self.col, self.row) , interpolation = cv2.INTER_AREA)

        # Define the RGB thresholds
        th_r = 20
        th_b = 20
        th_g = 60

        red_mask = self.cv_image[:,:,2] < th_b
        green_mask = self.cv_image[:,:,1] > th_g
        blue_mask = self.cv_image[:,:,0] < th_r

        color_mask = np.logical_and.reduce((red_mask, green_mask, blue_mask))

        self.result = np.any(color_mask)

        # Display the image
        cv2.imshow("color", self.cv_image)
        cv2.waitKey(3) 

# Main

if __name__ == '__main__':
# Camera object
    rospy.init_node('camera_node')
    cam = myCamera()

    rospy.spin()



