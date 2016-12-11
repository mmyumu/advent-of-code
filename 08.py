import sys
import re
import numpy as np


class Screen:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.matrix = [['.' for x in range(width)] for y in range(height)] 

	def drawRect(self, col, row):
		print "draw col=" + str(col) + ", row=" + str(row)
		for i in range(row):
			for j in range(col):
				self.matrix[i][j] = '#'

	def rotate(self, type, number, length):
		tempMatrix = [row[:] for row in self.matrix]

		if type == 'row':
			i = number
			for j in range(self.width):
				index = (j+self.width-length)%self.width
				self.matrix[i][j] = tempMatrix[i][index]
		elif type == 'column':
			j = number
			print "rotate col=" + str(j)
			for i in range(self.height):
				index = (i+self.height-length)%self.height
				self.matrix[i][j] = tempMatrix[index][j]
		else:
			raise NameError("Invalid rotation type. It shall be row or column: " + type)

	def printScreen(self):
		print np.matrix(self.matrix)

	def getPixelsLit(self):
		count = 0
		for i in range(self.height):
			for j in range(self.width):
				if self.matrix[i][j] == '#':
					count += 1
		return count
				

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "08.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
inputs = f.readlines()

screen = Screen(50, 6)
#screen = Screen(7, 3)

patternInstruction = re.compile("([a-z]+)\s(.*)")
patternRotation = re.compile("([a-z]+)\s(?:[a-z])=(\d+)\sby\s(\d+)")

patternRect = re.compile("(\d+)x(\d+)")
for input in inputs:
	instruction = patternInstruction.match(input)
	
	if instruction:
		if instruction.group(1) == "rect":
			rectInstruction = patternRect.match(instruction.group(2));
			if rectInstruction:
				screen.drawRect(int(rectInstruction.group(1)), int(rectInstruction.group(2)))
				#print "draw " + rectInstruction.group(1) + " by " + rectInstruction.group(2)
			else:
				raise NameError("Invalid rect format: " + input)
		elif instruction.group(1) == "rotate":
			rotationInstruction = patternRotation.match(instruction.group(2));
			if rotationInstruction:
				screen.rotate(rotationInstruction.group(1), int(rotationInstruction.group(2)), int(rotationInstruction.group(3)))
				#print "rotate " + rotationInstruction.group(1)
			else:
				raise NameError("Invalid rotation format: " + input)
		else:
			raise NameError("Instruction shall start with rect or rotate: " + input)
	else:
		raise NameError("Invalid instruction format: " + input)

	screen.printScreen()
	print "\n"

print "pixels lit:" + str(screen.getPixelsLit())