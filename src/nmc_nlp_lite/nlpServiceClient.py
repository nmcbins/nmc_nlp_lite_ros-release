#!/usr/bin/env python

import sys
import rospy
from nmc_nlp_lite.srv import *
import time
nlpService = rospy.ServiceProxy('nmc_nlp_service', nmcNLP)

def call_nmcNLPService(inputString):
    rospy.wait_for_service('nmc_nlp_service')
    try:
        resp1 = nlpService(inputString)
        return resp1.str
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

if __name__ == "__main__":
	while True:
		a=call_nmcNLPService("a male b")
		print "response:" + a
		time.sleep(1)