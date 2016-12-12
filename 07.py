import sys
import re

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "07.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
inputs = f.readlines()

supernetPattern = "([^\[]*)(\[([^\]]*)\]|\n)"
pattern = re.compile("(?P<char1>\w)(?P<char2>(?!(?P=char1))\w)(?P=char1).*----.*(?P=char2)(?P=char1)(?P=char2)")


count = 0
for input in inputs:
	if input[0] == "[":
		raise NameError('Cannot parse line starting with [')

	supernet = ""
	hypernet = ""
	for m in re.finditer(supernetPattern, input):
		if m.group(1):
			supernet += str(m.group(1)) + "-"
		if m.group(3):
			hypernet += str(m.group(3)) + "-"

	line = supernet + "---" + hypernet

	match = pattern.search(line)

	if match:
		print "Valid: " + input
		count += 1
	else:
		print "Invalid: " + input

print "Number of IPs: " + str(count)