# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:08:52 2019

@author: AlarshTiwari
"""
#openpyxl for raeding excel files

import argparse
import time
from naoqi import ALProxy
import sys
import math
import pandas as pd
import csv
import motion
import motions

def run(samples = 100):
    motions.stiff()
    motions.normalPose()
    timeStamp = time.time()
    checkLeft = True
    checkRight = True
    speech.say("Hello, I am overmind")
    while(True):
        (left, right) = getData(samples)
        print "Right:", right, "Left:", left
        
        if (wall(left, right)):
            print "Wall detected"
            if (checkLeft):
                print "Checking right"
                motions.walkTo((0, 0, -1.815))
                checkLeft = False
            elif (checkRight):
                print "Checking left"
                motions.walkTo((0, 0, 2.78))
                checkRight = False
                speech.say("I have escaped this maze like a boss")
            else:
                print "Checking back"
                motions.walkTo((0, 0, 1.39))
                
        else:
            print "Walking straight"
            motions.SWTV((0.5, 0, -0.0525, 0.8))
            checkLeft = True
            checkRight = True

def wall(left, right):
    if ((left < 42) and (right < 42)):
        return True
    return False

def getData(samples):
    totalL = 0
    totalR = 0
    for i in range(0, samples):
        sonarL = memory.getData(leftSonar,0)
        sonarR = memory.getData(rightSonar,0)
        totalL += sonarL
        totalR += sonarR
    return (totalL, totalR)    

def main(robot_IP, robot_PORT=9559):
    tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
    motion = ALProxy("ALMotion", robot_IP, robot_PORT)
    memory = ALProxy("ALMemory", robot_IP, robot_PORT)
    sonar = ALProxy("ALSonar", robot_IP, robot_PORT)
    postureProxy=ALProxy("ALRobotPosture", robot_IP, robot_PORT)
    tts.say("hello! I'm Michael")
    sonar.subscribe("myApplication",500,1.0)
    run()











if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--ip", type=str, default="169.254.", help="Robot ip address")
	parser.add_argument("--port", type=int, default=9559, help="Robot port number")
	args = parser.parse_args()
	main(args.ip, args.port)