import sys
import re

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "07.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
inputs = f.readlines()

abbaPattern = "(?P<char1>\w)(?P<char2>(?!(?P=char1))\w)(?P=char2)(?P=char1)"
#exclude = re.compile("\[[.^\]]*" + abbaPattern + "[.^\]]*\]")
exclude = re.compile("\[[^\]]*"+abbaPattern+"[^\]]*\]")
include = re.compile(abbaPattern)

count = 0
for input in inputs:
	excluded = exclude.search(input)
	if not excluded:
		print input
		included = include.search(input)
		if included:
			count += 1
		#else:
		#	print "not included=" + input
	else:
		print "excluded=" + input


print "Number of IPs: " + str(count)
