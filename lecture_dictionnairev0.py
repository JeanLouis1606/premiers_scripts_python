# exercice affichage de dictionnaire et message erreur

pets={'birds':3, 'cat':6, 'dog':5}
i=1
while i:
	print("entrer le nom d'un animal svp")
	name_animal=input()

	if name_animal in pets:
		nombre=pets.values()
		print(name_animal, nombre)
	elif name_animal not in pets :
		print("ce n'est pas dans la liste, recommencer svp")
		name_animal=input()
	
	