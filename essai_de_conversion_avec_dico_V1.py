#exercice avec dictionnaire de transfo chiffres romain arabe 

romain_arabe = {}
romain_arabe = {"M" : 1000, "D":500, "C":100, "L": 50, "X" :10, "V":5, "i":1}
print("nombre en chiffres romains ?") 
nombre= str(input()) #prend l'input en chaine de caractère 
print(len(nombre))

#conversion en chiffres arabes

i=0
number = 0 
while i < (len(nombre)):
	print("i",i)
	print("romain_arabe.get(nombre[i])", romain_arabe.get(nombre[i]))
	print("#######")
	#print("romain_arabe.get(nombre[i+1])", romain_arabe.get(nombre[i+1]))
	if (i < (len(nombre)) and (romain_arabe.get(nombre[i]) >= romain_arabe.get(nombre[i+1]))):
		number += romain_arabe.get(nombre[i])
		i+=1
		print("i",i)
		print("-------")
	elif i < (len(nombre)):
		number += (romain_arabe[nombre[i+1]] - romain_arabe.get(nombre[i]))
		i=i+2
	#number += romain_arabe.get(nombre[i])
print(number)







	
