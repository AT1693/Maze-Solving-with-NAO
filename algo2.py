# File day5.py by:
# Camiel Verschoor
# Sammy Odenhoven
# Tim van der Tuuk

from naoqi import ALProxy
import time
import motions
ip='169.254.177.99'
# Proxies
sonar = ALProxy("ALSonar",ip,9559)
memory = ALProxy("ALMemory",ip,9559)
speech = ALProxy("ALTextToSpeech",ip,9559)

# Sensors
leftSonar = "Device/SubDeviceList/US/Left/Sensor/Value"
rightSonar = "Device/SubDeviceList/US/Right/Sensor/Value"

# Subcribe to Sonar
sonar.subscribe("Sonar", 500, 1.0)

# Function
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

if __name__ == '__main__':
    run()