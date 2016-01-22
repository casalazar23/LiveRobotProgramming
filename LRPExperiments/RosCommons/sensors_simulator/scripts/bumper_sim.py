#!/usr/bin/env python
import rospy
from std_msgs.msg import Empty
from std_msgs.msg import Bool

isPressed = False

def bumperNotPressed():
    global isPressed
    pub = rospy.Publisher('sensors_simulator/sensors/bumper', Bool, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        if isPressed:
            for x in range(0,10): #10 loops ~ 1 seconds of sending a bumper pressed message
                pub.publish(True)
                rate.sleep()
            isPressed = False

        pub.publish(False)
        rate.sleep()

def pressBumper(data):
    global isPressed 
    isPressed = True

if __name__ == '__main__':
    try:
        rospy.init_node('bumper_sim', anonymous=True)
        rospy.Subscriber("sensors_simulator/actions/bump", Empty, pressBumper)
        bumperNotPressed()
    except rospy.ROSInterruptException:
        pass
