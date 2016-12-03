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
		count = 0

		tempDatas = []

		for data in self.datas:
			data = data.replace("\n", "")
			dataTokens = data.split();
			
			tempDatas.append(dataTokens)


			count += 1
			if count == 3:
				# Construct triangle here
				triangles.append(Triangle(tempDatas[0][0], tempDatas[1][0], tempDatas[2][0]))
				triangles.append(Triangle(tempDatas[0][1], tempDatas[1][1], tempDatas[2][1]))
				triangles.append(Triangle(tempDatas[0][2], tempDatas[1][2], tempDatas[2][2]))

				# Re init for next 3 rows
				count = 0
				tempDatas = []


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
