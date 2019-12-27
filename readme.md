Abstract—Maze-Solving Algorithm with NAO is a software developed specifically for the humanoid robot, NAO which gives it the capability to enter and exit a maze autonomously. NAO is a next -gen bot developed by the SoftBank Robotics using the power of AI. The bot is equipped with numerous sensors and cameras. The entire code is developed from scratch in Python language. Though various approaches were considered, we stuck onto the one which had the least average time complexity of all. AI constantly tries to give robots the human-thinking capabilities to make their decision-making skills equal to those of humans, if not better than them. This software was developed taking in care of how a human intellect would react rationally if stuck in such a maze. The methodology used revolves primarily around the use of SONAR sensors equipped with the bot. These output values from these sensors were used to judge the distance from a wall and the reactions from the bot were decided accordingly.


The approach which we finally decided to implement and upload onto our bot is the ’Wall Following Algorithm). The reason was that, when we tested all the above algorithms with mazes of different configuration, this was had the least average time taken. The algorithm is based on the idea of sticking to one wall and keep following its boundary. In most conditions, it guarantees an exit from the maze in a substantial time. The entire algorithm is implemented using Python language and using an SDK distributed by SoftBanks community.

The following is the Wall Following Algorithm implemented by us: -

If(Wall Detected):
	Turn Right
	If(Wall Detected):
		Turn Right
		If(Wall Detected):
			Turn Left
		Else:
			Move Forward
	Else:
		Move Forward
Else:
	Move Forward


The above implementation makes sure that the bot never stops at a dead end and keeps on searching for an exit. It also ensures that the bot is never stuck in a loop. The above algorithm is completely raw and in layman terms. In the actual algorithm, it includes implementation of the same using the functions and hardware activation of NAO using python scripts. This approach is tries to solve the maze in least average time possible for several mazes and gives highest average success probability in the time.


Though the immediate realization we may have after analyzing this project might not prove to be of much contribution to this field, but its one of the small steps taken towards a big direction of giving bots using AI, one of the very few things where humans surpasses them, Decision Making. The algorithm, if not the approach is completely novel, and we are in process of making further amends to our software to make it resistant to very few exceptional cases where it fails. 



The NAO bot was connected to the python script using two parameters, namely, the IP address and the port number. Firstly, we are required to connect our work machine (a laptop, here) to the NAO using an ethernet cable. Following is a python pseudo code for activating various hardware in the NAO.

tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
    motion = ALProxy("ALMotion", robot_IP, robot_PORT)
    memory = ALProxy("ALMemory", robot_IP, robot_PORT)
    sonar = ALProxy("ALSonar", robot_IP, robot_PORT)
    postureProxy=ALProxy("ALRobotPosture", robot_IP, robot_PORT)
sonar.subscribe("myApplication")
motion.wakeup()


We can then further build our algorithms using these or various other functionalities that naoqi offers for implementing python codes on NAO.


There were no datasets involved with this project. However, we did only two evaluation measures with which we measured the feasibility of any algorithm. The first was whether or not did the bot solve the maze and if yes, then the time it took to solve it.

The following is the time taken by various algorithms for a random maze structure.

Algorithm	Time Taken
	
Random Mouse	N.A.(Could not fetch results)
DFS	~25 min
Mapping	>1hour
Wall Following	18 min
