with open("/usr/share/dict/words") as inputfile:
	for line in inputfile:
		if len(line)<15:
			if (line[0] == 'x' and line[1] == 'y'):
				line = line.strip()
				print(line)
			
		