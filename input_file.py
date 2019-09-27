with open("/usr/share/dict/words") as inputfile:
	for line in inputfile:
		if line[0] == 'a': 
			line = line.strip()
			print(line)
			
		