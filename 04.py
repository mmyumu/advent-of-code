import sys
import re

class Room:
	def __init__(self, groups):
		print groups
		self.encryptedName = groups[0]
		self.sectorId = groups[1]
		self.checksum = groups[2]

	def isReal(self):
		previousCount = -1
		previousLetter = ''
		for letterToBeChecked in self.checksum:
			count = self.encryptedName.count(letterToBeChecked)
			# print "count of " + letterToBeChecked + "=" + str(count) + ", previousCount=" + str(previousCount)
			if previousCount != -1 and count > previousCount:
				return False
			previousCount = count
			previousLetter = letterToBeChecked

		for letterToBeChecked in self.encryptedName.replace("-", ""):
			checksumCount = self.checksum.count(letterToBeChecked)
			# print "checksumCount of "+letterToBeChecked+"=" + str(checksumCount)
			if checksumCount == 0:
				count = self.encryptedName.count(letterToBeChecked)
				if count > previousCount:
					return False
				elif count == previousCount and letterToBeChecked < previousLetter:
					return False

		return True


numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "04.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
inputs = f.readlines()

total = 0
for input in inputs:
	p = re.compile('((?:[a-z]+-)+)(\d+)\[([a-z]+)\]')
	m = p.match(input)

	room = Room(m.groups())
	if room.isReal() == True:
		print "real"
		total += int(room.sectorId)

print "Total: " + str(total)