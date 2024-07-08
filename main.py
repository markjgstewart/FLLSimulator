
from Tester import *

irSensor = IRSensor(Port.S3)
leftCS = ColorSensor(Port.S1)
rightCS = ColorSensor(Port.S2)
robot = DriveBase(Motor(Port.A),Motor(Port.B),10,10)
smallMotor = Motor(Port.C)

print("Start Commands")

#robot.straight(-200)

robot.turn(-30)
while leftCS.reflection()>8:
	robot.drive(500,0)
	#print("left reflection=",leftCS.reflection())

i=0
while i<50:
	robot.drive(30,leftCS.reflection()-30)
	i=i+1
while rightCS.reflection()>8:
	robot.drive(100,leftCS.reflection()-20)

robot.straight(40)
robot.turn(90)
robot.straight(70)
smallMotor.turn(-90)
robot.straight(-100)
smallMotor.turn(90)
robot.turn(180)
while leftCS.reflection()>8:
	robot.drive(200,0)



#while irSensor.distance()>-10:
#	robot.drive(50,0)
#	print(irSensor.distance())

#robot.turn(180)
#while irSensor.distance()>-10:
#	robot.drive(50,0)
#	print(irSensor.distance())
