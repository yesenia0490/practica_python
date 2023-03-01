import random
import os
intento = 0
a = "s"

while a == "s":
	os.system('clear')
	numero = random.randint(1,100)
	while True:
		print("adivina el numero del 1 al 100")
		num_user = int(input("Dame un numero: "))
		if numero == num_user:
			print (f'ganaste en el intentp {intento}')
			break;
		elif num_user > numero:
			print("el numero a adivinar es menor a:",num_user)
		else:
			print("el numero a adivinar es mayor a:",num_user)
		intento += 1
	print ("deseas volver a usar el programa")
	a = input ()
