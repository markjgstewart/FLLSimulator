#Numpy Light Substitute
#Mark Stewart 1-2022

def zeros(a):
	c=a[1]
	r=a[0]
	return ([[0]*c for i in range(r)])

def matmul(A,B):
	#print("A=",A)
	#print("B=",B)
	if not type(A[0]) is list:
		A = [A]
	if not type(B[0]) is list:
		B = [B]
	#print("multiply a ",len(A) ,"x",len(A[0])," by ",len(B) ,"x",len(B[0]) )
	if len(A[0])==len(B):
		#print("creating a ",len(A) ,"x",len(B[0]))
		C=zeros((len(A),len(B[0])))
		for r in range(len(A)):
			for c in range(len(B[0])):
				C[r][c]=0
				for i in range(len(A[0])):
					C[r][c]=C[r][c]+A[r][i]*B[i][c]
	else:
		print("ERROR, trying to multiply matrices of incompatiable sizes!")
	if len(C)==1:
		C=C[0]
	return C

def printM(A):
	for r in range(len(A)):
		print("| ",end='')
		for c in range(len(A[0])):
			print(A[r][c]," ", end='')
		print("|")
	print(" ")


def add(A,B,sign=1):
	#B must fit within A's size
	if not type(A[0]) is list:
		A = [A]
	if not type(B[0]) is list:
		B = [B]
	C=zeros((len(A),len(A[0])))
	for r in range(len(A)):
		for c in range(len(A[0])):
			C[r][c]=A[r][c]+sign*B[r][c]
	if len(C)==1:
		C=C[0]
	return C

def subtract(A,B):
	return add(A,B,-1)

def transpose(A):
	if not type(A[0]) is list:
		A = [A]
	C=zeros((len(A[0]),len(A)))
	for r in range(len(A)):
		for c in range(len(A[0])):
			C[c][r]=A[r][c]
	if len(C)==1:
		C=C[0]
	return C

#aa = zeros((2,3))
#aa=[[1,2,3],[4,5,6]]
#bb = zeros((3,1))
#bb=[[3],[0],[2]]
#printM(aa)
#printM(bb)
#c=transpose(aa)
#printM(c)
