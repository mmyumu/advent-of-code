import md5

doorId = "wtnhxymk"
#doorId = "abc"
password = ['-','-','-','-','-','-','-','-']

index = 0
count = 0
while count < 8:
	fullId = doorId + str(index)
	myMd5 = md5.new(fullId)

	hexdigest = myMd5.hexdigest()
	#print "Index: " + str(index) + " > Digest: " + hexdigest
	if hexdigest.startswith("00000") == True:
		try:
			position = int(hexdigest[5])
			if position <= 7 and password[position] == '-':
				print "Index: " + str(index) + ", hexdigest=" + hexdigest + " >> position=" + str(position)
				password[position] = hexdigest[6]
				print "Decrypting in progress [" + str(count) + "]: " + str(password)
				count += 1
		except:
			print "Index: " + str(index) + ", position not valid: " + hexdigest[5]

	index += 1

print "Decrypting done: " + str(password)