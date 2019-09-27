words=[]
with open("/usr/share/dict/words") as inputfile:
	for line in inputfile:
	
		if (line[0] == 'x' and line[1] == 'y'):
			line = line.strip()
			words.append(line)
	print(words[0], "#####")
	print(words , "\n")
	print(words[0], "#####")		
			
		