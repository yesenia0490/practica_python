import random
import os

def contraseña (longuitud):
	string = "|1234567890'¿qwertyuiopasdfghjklñ{}{<zxcvnbnmm,.-|1;:ÑU&$%=?/$~FAENBOPTGHKLECXZM**}[}+¬¬°"
	contras = ""
	
	while longuitud > 0:
		num_aleatorio = random.randint(0,len(string)-1)
		contras += string[num_aleatorio]
		longuitud -= 1
		
	return contras

while True:
	os.system("clear")
	print ("longuitud de contraseña")
	l = int(input())
	print (f'tu contraseña es: {contraseña(l)}')
	print ("desea generar otra contraseña")
	res = input()
	
	if res != 's':
		print ("bye")
		break;
		
