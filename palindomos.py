print (" escribe una palabra")

frase = input()

frase2 = ""

longuitud = len(frase) -1

while longuitud >= 0:
	frase2 += frase[longuitud]
	longuitud -= 1
	
print (frase2)

if frase2 == frase:
	print ("palindromo")
else:
	print (" no es palindromo")



