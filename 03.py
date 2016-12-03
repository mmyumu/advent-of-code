import sys

class Triangle:
	def __init__(self, a, b , c):
		self.a = int(a)
		self.b = int(b)
		self.c = int(c)

	def isValid(self):
		return (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)

class TriangleParser:
	def __init__(self, datas):
		self.datas = datas

	def getTriangles(self):
		triangles = []
		for data in self.datas:
			data = data.replace("\n", "")
			dataTokens = data.split();
			triangles.append(Triangle(dataTokens[0], dataTokens[1], dataTokens[2]))
		return triangles

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "03.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
triangleDatas = f.readlines()

triangleParser = TriangleParser(triangleDatas)
triangles = triangleParser.getTriangles()

valid = 0
notValid = 0
for triangle in triangles:
	print "triangle a=" + str(triangle.a) + ", b=" + str(triangle.b) + ", c=" + str(triangle.c)
	if triangle.isValid():
		valid += 1
	else:
		notValid += 1

print "Total triangles    : " + str(len(triangles))
print "Valid triangles    : " + str(valid)
print "Not valid triangles: " + str(notValid)
#for triangleInfo in triangleInfos:
#	
#
#	keyPressed = keypad.pressKey(instruction.replace("\n", ""))
#	print "Key pressed=" + str(keyPressed)