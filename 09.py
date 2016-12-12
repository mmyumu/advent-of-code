import sys
import re

markerPattern = re.compile("(\d+)x(\d+)")

class Marker:
	def __init__(self, startIndex, endIndex, subCharacters, times):
		self.startIndex = startIndex
		self.endIndex = endIndex
		self.subCharacters = subCharacters
		self.times = times

	def getFollowingIndex(self):
		return self.endIndex + self.subCharacters + 1




class Parser:
	def __init__(self, input, depth):
		self.input = input
		self.depth = depth

	def parse(self):
		index = 0
		count = 0
		print "[" + str(self.depth) + "] parse input=" + self.input
		while index < len(self.input):
			marker = self.parseMarker(index)
			if marker:
				print "[" + str(self.depth) + "] startIndex=" + str(marker.startIndex)
				print "[" + str(self.depth) + "] endIndex=" + str(marker.endIndex)
				print "[" + str(self.depth) + "] subChars=" + str(marker.subCharacters)
				subInput = self.input[marker.endIndex + 1:marker.getFollowingIndex()]

				parser = Parser(subInput, self.depth + 1)


				print "[" + str(self.depth) + "] index1=" + str(index)
				index = marker.getFollowingIndex()
				print "[" + str(self.depth) + "] index2=" + str(index)


				count += parser.parse() * marker.times
				#print marker.subCharacters
			else:
				index += 1
				count += 1
				
		print "[" + str(self.depth) + "] count=" + str(count)
		return count

	def parseMarker(self, index):
		markerStr = ""
		startIndex = index
		if self.input[index] == '(':
			index += 1
			currentCharacter = self.input[index]
			while currentCharacter != ')':
				markerStr += currentCharacter
				index += 1
				currentCharacter = self.input[index]

			marker = markerPattern.match(markerStr)
			if marker:
				return Marker(startIndex, index, int(marker.group(1)), int(marker.group(2)))
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

parser = Parser(input, 0)
count = parser.parse()

print "length=" + str(count)