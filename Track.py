
import Matrix as np
import random
import time

VERTICAL=1
HORIZONTAL=0

def createVLeg(tx,ty, track, debug=0):	
	temp = len(tx)
	for i in range(temp):
		tx = tx+[tx[(temp-1-i)]+20]
		ty= ty+[ty[(temp-1-i)]]
	t=list(zip(tx,ty))
	
	for i in range(temp-1):
		slope = (tx[i+1]-tx[i])/(ty[i+1]-ty[i])
		for yy in range(ty[i],ty[i+1]):
			xline = int(tx[i]+slope*(yy-ty[i]))
			#print("setting",xline,":",yy," txi=",tx[i])
			for j in range(20):
				track[xline+j][yy]=5
				track[xline-j][yy]=80
				track[xline+20+j][yy]=80
	return t

def createHLeg(tx,ty, track):
	temp = len(tx)
	for i in range(temp):
		tx = tx+[tx[(temp-1-i)]]
		ty= ty+[ty[(temp-1-i)]+20]
	t=list(zip(tx,ty))
	#print(t)

	for i in range(temp-1):
		#print("ty[i+1]=",ty[i+1],"ty[i]=",ty[i])
		slope = (ty[i+1]-ty[i])/(tx[i+1]-tx[i])
		#print("new H slope=",slope)
		for xx in range(tx[i],tx[i+1]):
			yline = int(ty[i]+slope*(xx-tx[i]))
			#print("setting",yline,":",xx," tyi=",ty[i])
			for j in range(20):
				track[xx][yline+j]=5
				track[xx][yline-j]=80
				track[xx][yline+20+j]=80
	return t

def createWhiteStrip(tx,ty):
	wxLeft=[]
	wxRight=[]
	wx = []
	wy=[]
	wyTop = []
	wyBot = []
	l=len(tx)
	for i in range(l):
		wxLeft = wxLeft+[tx[i]]
		wxRight = wxRight+[tx[i]+20]
		wx= wx+[tx[i]]
		wy= wy+[ty[i]]
		wyTop= wyTop+[ty[i]]
		wyBot= wyBot+[ty[i]+20]
	for i in range(l):
		wxLeft = wxLeft+[tx[l-1-i]-20]
		wxRight = wxRight+[tx[l-1-i]+20+20]
		wx= wx+[tx[l-1-i]]
		wy= wy+[ty[l-1-i]]
		wyTop= wyTop+[ty[l-1-i]-20]
		wyBot= wyBot+[ty[l-1-i]+20+20]
	wL=list(zip(wxLeft,wy))
	wR=list(zip(wxRight,wy))
	wT=list(zip(wx,wyTop))
	wB=list(zip(wx,wyBot))
	return [wL,wR,wT,wB]

def createTrack(w,h,canvas):
	print("creating track..")
	track = np.zeros((w,h))
	for x in range(w):
		for y in range(h):
			track[x][y]=random.randint(20,80)

	tx=[50,50,100]
	ty=[0,200,250]
	drawLeg(VERTICAL,tx,ty,track,canvas)
	tx=[400,400,420]
	ty=[0,400,500]
	drawLeg(VERTICAL,tx,ty,track,canvas)
	tx=[275,405] #x-values
	ty=[460,460] #y-values
	drawLeg(HORIZONTAL,tx,ty,track,canvas)
	tx=[435,535] #x-values
	ty=[50,50] #y-values
	drawLeg(HORIZONTAL,tx,ty,track,canvas)

	#add missions
	canvas.create_rectangle(550-5,50-5,550+5,50+5,fill='blue')
	canvas.create_rectangle(100-5,150-5,100+5,150+5,fill='blue')
	return track

def drawLeg(direction,tx,ty,track,canvas,debug=0):
	if direction==VERTICAL:
		t1=createVLeg(tx,ty,track,debug)
	else:
		t1=createHLeg(tx,ty,track)
	w1 = createWhiteStrip(tx,ty)
	canvas.create_polygon(t1,fill='black')
	canvas.create_polygon(w1[0],fill='white')
	canvas.create_polygon(w1[1],fill='white')
