print ("escribe algo")

string_original = input()

print("mostrar caracrter por caracter")

posicion_string = 0
tamaño_string = len(string_original)

while posicion_string < tamaño_string:
	caracter = string_original[posicion_string]
	print (f'en la posicion {posicion_string}, esta el caracter: {caracter}')
	posicion_string += 1
	
string_inverso = ""
tamaño_string -=1

while tamaño_string >= 0:
	string_inverso += string_original[tamaño_string]
	tamaño_string -=1

print ("este es el string inverso: ", string_inverso)
