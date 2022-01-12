#!/usr/bin/python2
import os
import sys

import rospy

import cv2
import cv_bridge

from sensor_msgs.msg import (
    Image,
)
from std_msgs.msg import (
    String,
)


def send_image(path):
    img = cv2.imread(path)
    msg = cv_bridge.CvBridge().cv2_to_imgmsg(img, encoding="bgr8")
    pub = rospy.Publisher('/robot/xdisplay', Image, latch=True, queue_size=1)
    pub.publish(msg)
    rospy.sleep(1)


def show(File):
    epilog = """
Notes:
    Max screen resolution is 1024x600.
    Images are always aligned to the top-left corner.
    Image formats are those supported by OpenCv - LoadImage().
    """
    delay = 0

    if not os.access(File, os.R_OK):
        rospy.logerr("Cannot read file at '%s'" % (File))
        return 1
    # Wait for specified time
    if delay > 0:
        rospy.loginfo(
            "Waiting for %s second(s) before publishing image to face" %
            (delay,)
        )
        rospy.sleep(delay)
    send_image(File)
    return 0

def callback(data):
    if data.data == "wan":
        File = "wan.png"
        show(File)
    if data.data == "nh":
        File = "nh.png"
        show(File)
    if data.data == "xxn":
        File = "xxn.png"
        show(File)
    if data.data == "bkq":
        File = "bkq.png"
        show(File)
    if data.data == "gx":
        File = "gx.png"
        show(File)
    if data.data == "mx":
        File = "mx.png"
        show(File)
    if data.data == "wj":
        File = "wj.png"
        show(File)

def display():
    while not rospy.is_shutdown():
        rospy.init_node('rsdk_xdisplay_image', anonymous=True)
        rospy.Subscriber("tcptopic", String, callback)
        rospy.spin()

if __name__ == '__main__':
    display()
