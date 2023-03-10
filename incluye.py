def incluye (frase, letra):
	resul = False
	lon = len(frase)
	cont = 0
	while cont < lon:
		if frase[cont] == letra:
			resul= True
		cont += 1
	return resul

print(incluye("gorda","s"))
print(incluye("gorda","o"))
