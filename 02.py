import sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class Key(Point):
	def __init__(self, x, y, label):
		Point.__init__(self, x, y)
		self.label = label


class Keypad:
	def __init__(self):
		# (0, 0) is TOP LEFT (so key 1) of the Keypad
		# 1 2 3
		# 4 5 6
		# 7 8 9
		
		self.currentPosition = Point(2, 0) # Key 5
		
	def pressKey(self, instruction):
		for movement in instruction:
			self.move(movement)
		return self.getCurrentKey().label
		
	def move(self, movement):
		if movement == "U":
			newPosition = Point(self.currentPosition.x - 1, self.currentPosition.y )
		elif movement == "D":
			newPosition = Point(self.currentPosition.x + 1, self.currentPosition.y)
		elif movement == "L":
			newPosition = Point(self.currentPosition.x, self.currentPosition.y - 1)
		elif movement == "R":
			newPosition = Point(self.currentPosition.x, self.currentPosition.y + 1)
		else:
			raise Exception("Incorrect movement: it should be U, D, L or R but it is " + movement)

		if self.checkLimits(newPosition) == True:
			self.currentPosition = newPosition
			#print "move to x=" + str(newPosition.x) + ", y=" + str(newPosition.y)
		#else:
			#print "cannot move to x=" + str(newPosition.x) + ", y=" + str(newPosition.y)


	def checkLimits(self, newPosition):
		key = self.getKey(newPosition)
		return key != 0
		#for allowedKey in allowedKeys:
		#	if allowedKey.x == newPosition.x and allowedKey.y == newPosition.y:
		#		return True
		#return False

	def getCurrentKey(self):
		return self.getKey(self.currentPosition)

	def getKey(self, position):
		for allowedKey in allowedKeys:
			if allowedKey.x == position.x and allowedKey.y == position.y:
				return allowedKey
		return 0

#allowedPositions = [Point(0,0), Point(0,1),Point(0,2),
#					Point(1,0),Point(1,1),Point(1,2),
#					Point(2,0),Point(2,1),Point(2,2)]

allowedKeys = [									Key(0,2,"1"), 
								  Key(1,1,"2"), Key(1,2,"3"), Key(1,3,"4"),
					Key(2,0,"5"), Key(2,1,"6"), Key(2,2,"7"), Key(2,3,"8"), Key(2,4,"9"),
								  Key(3,1,"A"), Key(3,2,"B"), Key(3,3,"C"),
												Key(4,2,"D")]

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "02.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
keypad = Keypad()

instructions = f.readlines()

for instruction in instructions:
	keyPressed = keypad.pressKey(instruction.replace("\n", ""))
	print "Key pressed=" + str(keyPressed)