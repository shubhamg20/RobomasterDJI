#!/usr/bin/env python
import cv2
import numpy as np
from cv_bridge import CvBridge,CvBridgeError
import rospy
from sensor_msgs.msg import Image

#trackbar callback fucntion to update HSV value
def get_img_data(data):        
        frame =CvBridge().imgmsg_to_cv2(data, "bgr8")
        return frame
def callback(x):
    global H_low,H_high,S_low,S_high,V_low,V_high
	#assign trackbar position value to H,S,V High and low variable
    H_low = cv2.getTrackbarPos('low H','controls')
    H_high = cv2.getTrackbarPos('high H','controls')
    S_low = cv2.getTrackbarPos('low S','controls')
    S_high = cv2.getTrackbarPos('high S','controls')
    V_low = cv2.getTrackbarPos('low V','controls')
    V_high = cv2.getTrackbarPos('high V','controls')
    print("in callback")  
def chnge_frame(frame):
    #create a seperate window named 'controls' for trackbar
    global H_low,H_high,S_low,S_high,V_low,V_high
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_low = np.array([H_low, S_low, V_low], np.uint8)
    hsv_high = np.array([H_high, S_high, V_high], np.uint8)

    #making mask for hsv range
    mask = cv2.inRange(hsv, hsv_low, hsv_high)
    cv2.imshow('mask', mask)
    cv2.imshow('frame', frame)
    #masking HSV value selected color becomes black
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #show image
    return res
rospy.init_node('image_tracker', anonymous=True)
bridge=CvBridge()
pub=rospy.Publisher("img_topic_1",Image,queue_size=1)
cv2.namedWindow('controls')
#cv2.resizeWindow("controls", 550,10)


#global variable
H_low = 0
H_high = 179
S_low= 0
S_high = 255
V_low= 0
V_high = 255

#create trackbars for high,low H,S,V 
cv2.createTrackbar('low H','controls',0,179,callback)
cv2.createTrackbar('high H','controls',179,179,callback)

cv2.createTrackbar('low S','controls',0,255,callback)
cv2.createTrackbar('high S','controls',255,255,callback)

cv2.createTrackbar('low V','controls',0,255,callback)
cv2.createTrackbar('high V','controls',255,255,callback)
while 1:
    msg=rospy.wait_for_message('/camera/color/image_raw',Image)
    frame=get_img_data(msg)
    frame=chnge_frame(frame)
    try:
        pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
    except CvBridgeError as e:
        print(e)

	
#destroys all window
cv2.destroyAllWindows()