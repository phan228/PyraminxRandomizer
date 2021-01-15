from array import *
import random

def Print(red, yellow, green, blue):
	(rows,cols) = (8,21)
	pyraminx = [[' ' for i in range(cols)] for j in range(rows)]
	for i in range(4):
		for j in range(0, 7):
			pyraminx[i][j] = red[i][j]
		for j in range(7, 14):
			pyraminx[i][j] = yellow[i][j-7]
		for j in range(14, 21):
			pyraminx[i][j] = green[i][j-14]
	for i in range(4, 8):	
		for j in range(7,14):
			pyraminx[i][j] = blue[i-4][j-7]
			
	for row in pyraminx:
		print(row)

# Tip rotations
def U1(red, yellow, green):
	temp = red[0][3]
	red[0][3] = yellow[0][3]
	yellow[0][3] = green[0][3]
	green[0][3] = temp

def L1(red, yellow, blue):
	temp = blue[0][0]
	blue[0][0] = yellow[3][0]
	yellow[3][0] = red[3][6]
	red[3][6] = temp

def R1(yellow, green, blue):
	temp = yellow[3][6]
	yellow[3][6] = blue[0][6]
	blue[0][6] = green[3][0]
	green[3][0] = temp

def B1(red, green, blue):
	temp = blue[3][3]
	blue[3][3] = green[3][6]
	green[3][6] = red[3][0]
	red[3][0] = temp

def U1_inv(red, yellow, green):
	U1(red, yellow, green)
	U1(red, yellow, green)

def L1_inv(red, yellow, blue):
	L1(red, yellow, blue)
	L1(red, yellow, blue)

def R1_inv(yellow, green, blue):
	R1(yellow, green, blue)
	R1(yellow, green, blue)

def B1_inv(red, green, blue):
	B1(red, green, blue)
	B1(red, green, blue)

# 2-layer rotations
def U2(red, yellow, green):
	U1(red,yellow,green)
	for i in range(2,5):
		temp = red[1][i]
		red[1][i] = yellow[1][i]
		yellow[1][i] = green[1][i]
		green[1][i] = temp

def L2(red, yellow, blue):
	L1(red, yellow, blue)
	temp = [yellow[2][1], yellow[3][2], yellow[3][3]]
	yellow[2][1] = red[3][4]
	yellow[3][1] = red[3][5]
	yellow[3][2] = red[2][5]
	
	red[3][4] = blue[0][2]
	red[3][5] = blue[0][1]
	red[2][5] = blue[1][1]

	blue[0][2] = temp[0]
	blue[0][1] = temp[1]
	blue[1][1] = temp[2]

def R2(yellow, green, blue):
	R1(yellow, green, blue)
	temp = [green[2][1], green[3][1], green[3][2]]
	green[2][1] = yellow[2][5]
	green[3][1] = yellow[3][5]
	green[3][2] = yellow[3][4]

	yellow[2][5] = blue[0][4]
	yellow[3][5] = blue[0][5]
	yellow[3][4] = blue[1][5]
	
	blue[1][5] = temp[0]
	blue[0][5] = temp[1]
	blue[0][4] = temp[2]

def B2(red, green, blue):
	B1(red, green, blue)
	temp = [red[2][1], red[3][1], red[3][2]]
	red[2][1] = blue[2][2]
	red[3][1] = blue[2][3]
	red[3][2] = blue[2][4]
	
	blue[2][2] = green[3][4]
	blue[2][3] = green[3][5]
	blue[2][4] = green[2][5]
	
	green[3][4] = temp[0] 
	green[3][5] = temp[1]
	green[2][5] = temp[2]

def U2_inv(red, yellow, green):
	U2(red, yellow, green)
	U2(red, yellow, green)
		
def L2_inv(red, yellow, blue):
	L2(red, yellow, blue)
	L2(red, yellow, blue)

def R2_inv(yellow, green, blue):
	R2(yellow, green, blue)
	R2(yellow, green, blue)

def B2_inv(red, green, blue):
	B2(red, green, blue)
	B2(red, green, blue)

# 3-layer rotations
def U3(red, yellow, green):
	U2(red, yellow, green)
	for j in range(1,7):
		temp = red[2][j]
		red[2][j] = yellow[2][j]
		yellow[2][j] = green[2][j]
		green[2][j] = temp

def L3(red, yellow, blue):
	L2(red, yellow, blue)
	temp = [red[3][2], red[3][3], red[2][3], red[2][4], red[1][4]]
	red[3][2] = blue[0][4]
	red[3][3] = blue[0][3]
	red[2][3] = blue[1][3]
	red[2][4] = blue[1][2]
	red[1][4] = blue[2][2]

	blue[0][4] = yellow[1][2]
	blue[0][3] = yellow[2][2]
	blue[1][3] = yellow[2][3]
	blue[1][2] = yellow[3][3]
	blue[2][2] = yellow[3][4]

	yellow[1][2] = temp[0]
	yellow[2][2] = temp[1]
	yellow[2][3] = temp[2]
	yellow[3][3] = temp[3]
	yellow[3][4] = temp[4]

def R3(yellow, green, blue):
	R2(yellow, green, blue)
	temp = [yellow[3][2], yellow[3][3], yellow[2][3], yellow[2][4], yellow[1][4]]
	yellow[3][2] = blue[2][4]
	yellow[3][3] = blue[1][4]
	yellow[2][3] = blue[1][3]
	yellow[2][4] = blue[0][3]
	yellow[1][4] = blue[0][2]

	blue[2][4] = green[1][2]
	blue[1][4] = green[2][2]
	blue[1][3] = green[2][3]
	blue[0][3] = green[3][3]
	blue[0][2] = green[3][4]

	green[1][2] = temp[0]
	green[2][2] = temp[1]
	green[2][3] = temp[2]
	green[3][3] = temp[3]
	green[3][4] = temp[4]

def B3(red, green, blue):
	B2(red, green, blue)
	temp = [red[1][2], red[2][2], red[2][3], red[3][3], red[3][4]]
	red[1][2] = blue[1][1]
	red[2][2] = blue[1][2]
	red[2][3] = blue[1][3]
	red[3][3] = blue[1][4]
	red[3][4] = blue[1][5]

	blue[1][1] = green[3][2]
	blue[1][2] = green[3][3]
	blue[1][3] = green[2][3]
	blue[1][4] = green[2][4]
	blue[1][5] = green[1][4]

	green[3][2] = temp[0]
	green[3][3] = temp[1]
	green[2][3] = temp[2]
	green[2][4] = temp[3]
	green[1][4] = temp[4]

def U3_inv(red, yellow, green):
	U3(red, yellow, green)
	U3(red, yellow, green)

def L3_inv(red, yellow, blue):
	L3(red, yellow, blue)
	L3(red, yellow, blue)

def R3_inv(yellow, green, blue):
	R3(yellow, green, blue)
	R3(yellow, green, blue)

def B3_inv(red, green, blue):
	B3(red, green, blue)
	B3(red, green, blue)

def Main():
	# Creating a pyraminx
	(rows,cols) = (4,7)
	red = [[' ' for i in range(cols)] for j in range(rows)]
	yellow = [[' ' for i in range(cols)] for j in range(rows)]
	blue = [[' ' for i in range(cols)] for j in range(rows)]
	green = [[' ' for i in range(cols)] for j in range(rows)]

	# setup red face
	red[0][3] = red[1][2] = red[1][3] = red[1][4] = red[2][1] = red[2][2] = red[2][3] = red[2][4] = red[2][5]= 'R'
	for i in range(7):
		red[3][i] = 'R'

	# setup yellow face
	yellow[0][3] = yellow[1][2] = yellow[1][3] = yellow[1][4] = yellow[2][1] = yellow[2][2] = yellow[2][3] = yellow[2][4] = yellow[2][5]= 'Y'
	for i in range(7):
		yellow[3][i] = 'Y'

	# setup blue face
	blue[3][3] = blue[1][2] = blue[1][3] = blue[1][4] = blue[1][1] = blue[2][2] = blue[2][3] = blue[2][4] = blue[1][5]= 'B'
	blue[0][0] = 'B'
	for i in range(7):
		blue[0][i] = 'B'

	# setup green face
	green[0][3] = green[1][2] = green[1][3] = green[1][4] = green[2][1] = green[2][2] = green[2][3] = green[2][4] = green[2][5]= 'G'
	for i in range(7):
		green[3][i] = 'G'

	#Initial pyraminx
	print("The initial pyraminx:")
	Print(red, yellow, green, blue)

	# Randomize the pyraminx
	inp = input("Enter number of moves (0 to quit): ")
	move = int(inp)
	moveList = []
	moves = []

	for i in range(move):
		moveList.append(random.randint(1,24))
	
	for i in range(len(moveList)):
		if moveList[i] == 1:
			U1(red, yellow, green)
			moves.append("U1")
		elif moveList[i] == 2:
			L1(red, yellow, blue)
			moves.append("L1")
		elif moveList[i] == 3:
			R1(yellow, green, blue)
			moves.append("R1")
		elif moveList[i] == 4:
			B1(red, green, blue)
			moves.append("B1")
		elif moveList[i] == 5:
			U2(red, yellow, green)
			moves.append("U2")
		elif moveList[i] == 6:
			L2(red, yellow, blue)
			moves.append("L2")
		elif moveList[i] == 7:
			R2(yellow, green, blue)
			moves.append("R2")
		elif moveList[i] == 8:
			B2(red, green, blue)
			moves.append("B2")
		elif moveList[i] == 9:
			U3(red, yellow, green)
			moves.append("U3")
		elif moveList[i] == 10:
			L3(red, yellow, blue)
			moves.append("L3")
		elif moveList[i] == 11:
			R3(yellow, green, blue)
			moves.append("R3")
		elif moveList[i] == 12:
			B3(red, green, blue)
			moves.append("B3")
		elif moveList[i] == 13:
			U1_inv(red, yellow, green)
			moves.append("U1_inv")
		elif moveList[i] == 14:
			L1_inv(red, yellow, blue)
			moves.append("L1_inv")
		elif moveList[i] == 15:
			R1_inv(yellow, green, blue)
			moves.append("R1_inv")
		elif moveList[i] == 16:
			B1_inv(red, green, blue)
			moves.append("B1_inv")
		elif moveList[i] == 17:
			U2_inv(red, yellow, green)
			moves.append("U2_inv")
		elif moveList[i] == 18:
			L2_inv(red, yellow, blue)
			moves.append("L2_inv")
		elif moveList[i] == 19:
			R2_inv(yellow, green, blue)
			moves.append("R2_inv")
		elif moveList[i] == 20:
			B2_inv(red, green, blue)
			moves.append("B2_inv")
		elif moveList[i] == 21:
			U3_inv(red, yellow, green)
			moves.append("U3_inv")
		elif moveList[i] == 22:
			L3_inv(red, yellow, blue)
			moves.append("L3_inv")
		elif moveList[i] == 23:
			R3_inv(yellow, green, blue)
			moves.append("R3_inv")
		elif moveList[i] == 24:
			B3_inv(red, green, blue)
			moves.append("B3_inv")
	
	#print(moves)
	Print(red, yellow, green, blue)

if __name__ == '__main__':
	Main()
	
