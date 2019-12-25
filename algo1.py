
'''
@author: AlarshTiwari
'''
# File: rightRule.py
from naoqi import ALProxy
import time
import motions

# Proxies
sonar = ALProxy("ALSonar",'169.254.121.67',9559)
memory = ALProxy("ALMemory",'169.254.121.67',9559)

# Sensors
leftSonar = "Device/SubDeviceList/US/Left/Sensor/Value"
rightSonar = "Device/SubDeviceList/US/Right/Sensor/Value"

# Subcribe to Sonar
sonar.subscribe("Sonar", 500, 1.0)

# Stiff the NAO

def run(samples = 100):
    motions.stiff()
    motions.normalPose()
    timeStamp = time.time()
    check = True
    while(time.time() - timeStamp < 1000):
        (left, right) = getData(samples)
        print "Right:", right, "Left:", left
        deltaL = left - right
        deltaR = right - left
        print "DeltaR:", deltaR, "DeltaL:", deltaL
        if((left < 40) and (right < 40)):
            print "WALL DETECTED"
            if(check):
                print "CHECK RIGHT"
                motions.walkTo((0, 0, -1.33))
                check = False
            else:
                print "CHECK LEFT"
                motions.SWTV((0, 0, 0.25, 0.7))
        elif((right >= 40) and (left >= 40)):
            check = True
            print "WALKING STRAIGHT"
            motions.SWTV((0.5, 0, 0, 0.5))
        elif((deltaR < 0 and deltaR > -5)):
            print "ADJUST ANGLE TO LEFT"
            motions.SWTV((0.5, 0, 0.05, 0.5))
        elif((deltaL < 0 and deltaL > -5)):
            print "ADJUST ANGLE TO RIGHT"
            motions.SWTV((0.5, 0, -0.05, 0.5))
        else:
            print "STOP"
            motions.walkTo((0.01, 0, 0))

    print "STOP"
    motions.walkTo((0.01, 0, 0))
            
def getData(samples):
    totalL = 0
    totalR = 0
    for i in range(0, samples):
        sonarL = memory.getData(leftSonar,0)
        sonarR = memory.getData(rightSonar,0)
        totalL += sonarL
        totalR += sonarR
    return (totalL, totalR)

if __name__ == '__main__':
    run()