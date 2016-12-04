import sys
import re

class Room:
	def __init__(self, groups):
		self.encryptedName = groups[0]
		self.sectorId = int(groups[1])
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

	def decrypt(self):
		decryptedName = ""
		for letter in self.encryptedName:
			if letter == '-':
				decryptedName += " "
			else:
				letterAscii = ord(letter)
				letterAscii -= 97
				letterAscii += self.sectorId
				letterAscii = letterAscii%26
				letterAscii += 97
				decryptedName += chr(letterAscii)

		return decryptedName

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
		decryptedName = room.decrypt()
		if "north" in decryptedName:
			print "Decrypted name: " + room.decrypt()
			print "Sector ID: " + str(room.sectorId)