#Robot Simulation for FLL
#Mark Stewart 1-2022

from tkinter import *
import random
import time
import math
import Matrix as np
from Track import createTrack

track = []
WIDTH=600
HEIGHT=600

car=[50,500]
carW=40
carH=60	#this is the width
hammerW=20
hammer=[0,0]
carAngleRad=0
hammerAngleRad=math.pi/2
corner =[]
cornerHammer =[2,3]
box=[[550,50],[100,150]]
boxColor=['blue','blue']

def setCorners():
	global corner, cornerHammer, car, hammer
	hL=(carH/10)+0.1*carH*math.cos(hammerAngleRad)
	LL=30*math.cos(hammerAngleRad)

	hammer[0]=car[0]+(20+LL)*math.cos(carAngleRad)
	hammer[1]=car[1]+(20+LL)*math.sin(carAngleRad)
	corner=[ [car[0]-carW/2,car[1]-carH/2],[car[0]-carW/2,car[1]+carH/2],[car[0]+carW/2,car[1]+carH/2],[car[0]+carW/2,car[1]-carH/2]]
	cornerHammer=[ [hammer[0]-hL,hammer[1]-carH/4],[hammer[0]-hL,hammer[1]+carH/4],[hammer[0]+hL,hammer[1]+carH/4],[hammer[0]+hL,hammer[1]-carH/4]]
	R = np.zeros((2,2))
	R[0][0]=math.cos(carAngleRad)
	R[0][1]=-math.sin(carAngleRad)
	R[1][0]=math.sin(carAngleRad)
	R[1][1]=math.cos(carAngleRad)
	for i in range(4):
		temp1 = np.matmul(R,np.transpose(np.subtract(corner[i],car)))
		corner[i]= np.add( np.transpose(temp1),car)
		temp2 = np.matmul(R,np.transpose(np.subtract(cornerHammer[i],hammer)))
		cornerHammer[i]=np.add( np.transpose(temp2),hammer)
	checkBounds()
	#print("corners set")

def checkBounds():
	global corner,boardGUI
	#print("check bounds..",corner)
	for i in range(4):
		if corner[i][0]<0 or corner[i][1]<0 or corner[i][0]>WIDTH or corner[i][1]>HEIGHT:
			canvas.delete("all")
			star=[(200,200),(250,250),(300,200),(300,300),(400,325),(275,300),(250,400),(200,250),(100,250),(225,300)]
			canvas.create_polygon(star,fill='red')
			canvas.create_text(200,100,fill='black',text='Crashed into wall. You are done.')
			boardGUI.update()
			time.sleep(2)
			boardGUI.destroy()
			sys.exit("ending program")
def avg(x,y):
	return (x+y)/2	

def redraw():
	canvas.delete("cart")
	canvas.delete("leftCS")
	canvas.delete("rightCS")
	canvas.delete("hammer")
	canvas.delete("line")
	canvas.delete("leftWheel")
	canvas.delete("rightWheel")
	setCorners()
	canvas.create_polygon(corner[0][0],corner[0][1],corner[1][0],corner[1][1],corner[2][0],corner[2][1],corner[3][0],corner[3][1],fill='green',tag='cart')
	canvas.create_oval(corner[2][0]-3,corner[2][1]-3,corner[2][0]+3,corner[2][1]+3,fill='blue',tag='rightCS')
	canvas.create_oval(corner[3][0]-3,corner[3][1]-3,corner[3][0]+3,corner[3][1]+3,fill='red',tag='leftCS')

	leftWheel = [avg(corner[2][0],corner[1][0]),avg(corner[2][1],corner[1][1])]
	rightWheel =[avg(corner[0][0],corner[3][0]),avg(corner[0][1],corner[3][1])]
	canvas.create_oval(leftWheel[0]-3,leftWheel[1]-3,leftWheel[0]+3,leftWheel[1]+3,fill='yellow',tag='leftWheel')
	canvas.create_oval(rightWheel[0]-3,rightWheel[1]-3,rightWheel[0]+3,rightWheel[1]+3,fill='yellow',tag='rightWheel')

	canvas.create_polygon(cornerHammer[0][0],cornerHammer[0][1],cornerHammer[1][0],cornerHammer[1][1],cornerHammer[2][0],cornerHammer[2][1],cornerHammer[3][0],cornerHammer[3][1],fill='black',tag='hammer')
	canvas.create_line(hammer[0],hammer[1],car[0],car[1],width=3,tag='line')

	for i in range(len(box)):
		canvas.create_rectangle(box[i][0]-5,box[i][1]-5,box[i][0]+5,box[i][1]+5,fill=boxColor[i])

	boardGUI.update()

boardGUI=Tk()
boardGUI.title("FLL Board")
canvas = Canvas(boardGUI,width=WIDTH,height=HEIGHT)
canvas.grid(column=10,row=10)
canvas.create_text(300,575,fill="black",font="Times 10 bold", text="GOAL. Hit the two blue squares with the hammer. They will turn yellow.")
track = createTrack(WIDTH,HEIGHT,canvas)
setCorners()
canvas.create_polygon(corner[0][0],corner[0][1],corner[1][0],corner[1][1],corner[2][0],corner[2][1],corner[3][0],corner[3][1],fill='green',tag='cart')
boardGUI.update()
time.sleep(1)

class DriveBase:
	def __init__(self, leftMotor, rightMotor, radius, spacing):
		print("init drivebase...",car[0])
	def drive(self, power, turn):
		global car, carAngleRad
		if power>200:
			power=200
		if power<-200:
			power=-200
		power=power+power*.01*random.randint(-10,10)
		carAngleRad=carAngleRad+turn/500+(random.randint(-5,5))*0.01745/10
		car[0]=car[0]+math.cos(carAngleRad)*power/20
		car[1]=car[1]+math.sin(carAngleRad)*power/20
		redraw()
		time.sleep(0.02)
	def turn(self, angleDeg):
		global car
		global carAngleRad
		for i in range(10): #break turn into 10 pieces
			carAngleRad=carAngleRad+(angleDeg+random.randint(-3,3))*0.01745/10
			time.sleep(0.1)
			redraw()
		#print("turning...")
		redraw()
	def straight(self, amount):
		global car
		global carAngleRad
		power=100+random.randint(-10,10)
		if amount<0:
			amount=-amount
			power=-power
		i=0
		while i<amount/5:
			carAngleRad=carAngleRad+(random.randint(-5,5))*0.01745/10
			car[0]=car[0]+math.cos(carAngleRad)*power/20
			car[1]=car[1]+math.sin(carAngleRad)*power/20
			#print("driving..")
			redraw()
			time.sleep(0.1)
			i=i+1

class ColorSensor:
	LEFT=3
	RIGHT=2
	def __init__(self, lOrR):
		self.leftOrRight = lOrR
	def reflection(self):
		global track
		sum=0
		for x in range(-5,5):
			for y in range(-5,5):
				sum = sum + track[int(corner[self.leftOrRight][0])+x][int(corner[self.leftOrRight][1])+y]
		time.sleep(0.02)
		return sum/100

class IRSensor:
	def __init__(self, pA):
		print("initialize IR Sensor")
	def distance(self):
		global carAngleRad
		while carAngleRad > 6.2832:
			carAngleRad = carAngleRad - 6.2832
		distance=1000
		front = [(corner[3][0]+corner[2][0])/2,(corner[3][1]+corner[2][1])/2]
		field=30*3.14/180

		if carAngleRad<(0+field) and carAngleRad > (0-field):
			distance=(WIDTH-front[0])/math.cos(carAngleRad-0)

		if carAngleRad<(math.pi/2+field) and carAngleRad > (math.pi/2-field):
			distance=(HEIGHT-front[1])/math.cos(carAngleRad-math.pi/2)

		if carAngleRad<(math.pi+field) and carAngleRad > (math.pi-field):
			distance=(front[0])/math.cos(carAngleRad-3.141)

		if carAngleRad<(3*math.pi/2+field) and carAngleRad > (3*math.pi/2-field):
			distance=(front[1])/math.cos(carAngleRad-3*math.pi/2)
		return distance
		

class Port:
	S1=3 #left
	S2=2 #right
	S3=1 #IR sensor
	A=0 #left motor
	B=1 #right motor
	C=2 #small motor

def shiftCar(car, a):
	#print("car angle:",carAngleRad*180/3.14)
	#print("car x,y",car[0]," ",car[1])
	car[0]=car[0]+a*(carH/2)*math.cos(math.pi/2+carAngleRad) #car angle defined oddly because y is down
	car[1]=car[1]+a*(carH/2)*math.sin(math.pi/2+carAngleRad)

class Motor:
	def __init__(self, port):
		self.motorType= port
		print("initialize motor: ",self.motorType)
	def turn(self, angleDeg):
		global hammerAngleRad, hammer, box, boxColor, carAngleRad
		if self.motorType==Port.C:		
			for i in range(10):
				hammerAngleRad=hammerAngleRad+(angleDeg+random.randint(-3,3))*0.01745/10
				time.sleep(0.1)
				redraw()
			redraw()
			#mission specific code, check objective boxes, needs to be only for small motor
			if hammerAngleRad < (30*0.0175) and hammerAngleRad>0 and angleDeg < 0:		
				for i in range(len(box)):
					error = (hammer[0]-box[i][0])*(hammer[0]-box[i][0])+(hammer[1]-box[i][1])*(hammer[1]-box[i][1])
					if error<200:
						boxColor[i]='yellow'
		if self.motorType==Port.A:
			for i in range(10): #break turn into 10 pieces
				shiftCar(car, 1)
				carAngleRad=carAngleRad+(angleDeg+random.randint(-3,3))*0.01745/10
				shiftCar(car, -1)
				redraw()	
				time.sleep(.05)
				
			#print("turning...")
			redraw()
		if self.motorType==Port.B:
			for i in range(10): #break turn into 10 pieces
				shiftCar(car, -1)
				carAngleRad=carAngleRad+(-angleDeg+random.randint(-3,3))*0.01745/10
				shiftCar(car, 1)
				redraw()	
				time.sleep(.05)
				
			#print("turning...")
			redraw()

