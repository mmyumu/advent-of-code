import sys
import re

markerPattern = re.compile("(\d+)x(\d+)")

class Marker:
	def __init__(self, endIndex, subCharacters, times):
		self.endIndex = endIndex
		self.subCharacters = subCharacters
		self.times = times

	def getFollowingIndex(self):
		return self.endIndex + self.subCharacters




class Parser:
	def __init__(self, input):
		self.input = input
		#self.index = 0
		#self.result = ""

	def parse(self):
		result = ""
		index = 0
		while index < len(self.input):
			marker = self.parseMarker(index)
			if not marker == False:
				result += self.decompressMarker(marker)
				index = marker.getFollowingIndex()
			else:
				result += self.input[index]
			index += 1

		return result

	def parseMarker(self, index):
		markerStr = ""
		if self.input[index] == '(':
			index += 1
			currentCharacter = self.input[index]
			while currentCharacter != ')':
				markerStr += currentCharacter
				index += 1
				currentCharacter = self.input[index]

			marker = markerPattern.match(markerStr)
			if marker:
				return Marker(index, int(marker.group(1)), int(marker.group(2)))
		return False

	def decompressMarker(self, marker):
		result = ""

		#print "decompress between " + str(marker.endIndex) + " and " + str(marker.endIndex + marker.subCharacters)
		for numberOfTimes in range(marker.times):
			for index in range(marker.endIndex + 1, marker.endIndex + marker.subCharacters + 1):
				result += self.input[index]

		return result;

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "09.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
inputs = f.readlines()

input = ""
result = ""
for inputLine in inputs:
	input += inputLine.replace("\n", "").replace(" ", "")

parser = Parser(input)
decompressedMsg = parser.parse()
print decompressedMsg
print "length=" + str(len(decompressedMsg))