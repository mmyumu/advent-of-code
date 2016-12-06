import sys

numberOfArgs = len(sys.argv)

if(numberOfArgs == 1):
	inputFile = "06.txt"
elif(numberOfArgs == 2):
	inputFile = sys.argv[1]

f = open(inputFile, 'r')
inputs = f.readlines()

password = ['-', '-', '-', '-', '-', '-', '-', '-']

for position in range(8):
	letterCount = {}
	for input in inputs:
		letter = input[position]
		if letter in letterCount:
			letterCount[letter] += 1	
		else:
			letterCount[letter] = 1

	print letterCount

	max = 0
	for letter, count in letterCount.iteritems():
		if count > max:
			password[position] = letter
			max = count
		#print "letter=" + letter + ", count=" + str(count)


print password

