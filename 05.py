import md5

doorId = "wtnhxymk"
#doorId = "abc"
password = ""


index = 0
for letter in doorId:
	found = False
	while found == False:
		fullId = doorId + str(index)
		myMd5 = md5.new(fullId)

		hexdigest = myMd5.hexdigest()
		#print "Index: " + str(index) + " > Digest: " + hexdigest
		if hexdigest.startswith("00000") == True:
			print "Index: " + str(index) + ", hexdigest=" + hexdigest
			password += hexdigest[5]
			found = True
		index += 1

print password