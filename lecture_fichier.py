print("donner le fichier à lire svp")
name = input()
with open(name) as fichier:
	for ligne in fichier:
		print(ligne)
		