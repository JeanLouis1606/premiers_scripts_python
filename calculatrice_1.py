#calculatrice Python
nombre = 0
i=0
while i==0:
	try:
		print("entrer une valeur ")
		nombre += int(input())
		print(nombre)
	except ValueError:
		nombre = None
		print(" ce n'est pas un nombre connu")
	except NameError:
		print("un problème de code")
	except: 
		print("problème inconnu")
	
	
