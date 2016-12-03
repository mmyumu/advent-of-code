import sys

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class Keypad:
	def __init__(self):
		# (0, 0) is TOP LEFT (so key 1) of the Keypad
		# 1 2 3
		# 4 5 6
		# 7 8 9
		
		self.currentPosition = Point(1, 1) # Key 5
		
	def pressKey(self, instruction):
		for movement in instruction:
			self.move(movement)
		return self.getKeypadNumber()
		
	def move(self, movement):
		if movement == "U":
			self.currentPosition.y -= 1
		elif movement == "D":
			self.currentPosition.y += 1
		elif movement == "L":
			self.currentPosition.x -= 1
		elif movement == "R":
			self.currentPosition.x += 1
		self.checkLimits()

	def checkLimits(self):
		if self.currentPosition.x < 0:
			self.currentPosition.x = 0
		if self.currentPosition.x > 2:
			self.currentPosition.x = 2
		if self.currentPosition.y < 0:
			self.currentPosition.y = 0
		if self.currentPosition.y > 2:
			self.currentPosition.y = 2

	def getKeypadNumber(self):
		print "Convert from x=" + str(self.currentPosition.x) + ", y=" + str(self.currentPosition.y)
		return self.currentPosition.y * 3 + self.currentPosition.x + 1

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "02.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
keypad = Keypad()

instructions = f.readlines()

for instruction in instructions:
	keyPressed = keypad.pressKey(instruction)
	print "Key pressed=" + str(keyPressed)