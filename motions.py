# File day5.py by:
# Camiel Verschoor
# Sammy Odenhoven
# Tim van der Tuuk
# Thanks to Dutch Nao Team for the following functions

# motions implements the motionInterface
from naoqi import ALProxy
import time
import math


motion = ALProxy('ALMotion', '169.254.121.67', 9559)
pose = ALProxy('ALRobotPosture', '169.254.121.67', 9559)

# activate stiffness
def stiff():
        motion.setStiffnesses('Body', 0.925)
        # to prevent further damage, low stiffness for the head. 
        motion.setStiffnesses('HeadPitch', 0.5)
        motion.setStiffnesses('HeadYaw', 0.5)
        
# ##### Walking ######
# setWalkTargetVelocity 
def SWTV((x,y,t,f)):
        motion.setWalkTargetVelocity(x,y,t,f)

# blocking walk call
def walkTo((x,y,angle)):
        motion.walkTo(x,y,angle)
                        
def normalPose():
        names = list()
        times = list()
        angles = list()
        
       # if getPose()=='Stand':
       #     return True
        
        names.append('HeadPitch')
        times.append([1])
        angles.append([ [ -0.5 , [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])             
                
        names.append('HeadYaw')
        times.append([1])
        angles.append([ [ 0.0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])
        
        names.append('LShoulderPitch')
        times.append([1])
        angles.append([ [ 1.2, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LShoulderRoll')
        times.append([1])
        angles.append([ [ 0.15, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LElbowYaw')
        times.append([1])
        angles.append([ [ 0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LElbowRoll')
        times.append([1])
        angles.append([ [ 0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RShoulderPitch')
        times.append([1])
        angles.append([ [ 1.2, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RShoulderRoll')
        times.append([1])
        angles.append([ [ -0.15, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RElbowYaw')
        times.append([1])
        angles.append([ [ 0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RElbowRoll')
        times.append([1])
        angles.append([ [ 0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LHipYawPitch')
        times.append([1])
        angles.append([ [ 0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LHipRoll')
        times.append([1])
        angles.append([ [ 0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LHipPitch')
        times.append([1])
        angles.append([ [ -0.4, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LKneePitch')
        times.append([1])
        angles.append([ [ 0.95, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LAnklePitch')
        times.append([1])
        angles.append([ [ -0.55, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('LAnkleRoll')
        times.append([1])
        angles.append([ [ 0.0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RHipRoll')
        times.append([1])
        angles.append([ [ 0.0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RHipPitch')
        times.append([1])
        angles.append([ [ -0.4, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RKneePitch')
        times.append([1])
        angles.append([ [ 0.95, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RAnklePitch')
        times.append([1])
        angles.append([ [ -0.55, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        names.append('RAnkleRoll')
        times.append([1])
        angles.append([ [ 0.0, [ 3, -1.00000, 0.00000], [ 3, 0.00000, 0.00000]]])

        motion.post.angleInterpolationBezier(names, times, angles)