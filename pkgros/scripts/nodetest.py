#!/usr/bin/env python
import roslib
import rospy

class TestNode():
	def __init__(self, topic='topic_test'):
		self.pub = rospy.Publisher(topic, String)
		self.time_sleep = 1
	
	def main_loop(self):
		while not rospy.is_shutdown():
			self.pub.publish()
			rospy.sleep(self.time_sleep)

if __name__ == "__main__":
	print "Test of ROS"
	print "What is your age?"
	age = input()
	print "You are ", age, "yo"

