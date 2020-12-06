from colorama import init, Fore
import numpy as np
import os

def borrarPantalla(): 
	if os.name == "posix":
	   os.system ("clear")
	elif os.name == "ce" or os.name == "nt" or os.name == "dos":
	   os.system ("cls")

def printMat(mat, Op, color, renglon):
	borrarPantalla()
	if Op==-1:
		if color == -1:
			print("\nLos renglones con color "+Fore.BLUE+" Azul"+Fore.WHITE+", suman 1.")
			print("Los renglones con color "+Fore.RED+" Rojo"+Fore.WHITE+", No suman 1.")
			print("Los renglones con color 'Blanco', aún no se revisan."+Fore.BLUE)
		else:
			print("\nLa matriz de transición es: "+Fore.BLUE)
		
		for i in range(len(mat)):
			for j in range(len(mat[i])):
				if color == -1 and renglon==i:
					print(Fore.RED+"", end="")
					print ('{:>4s}'.format(str(mat[i][j]))+'{:>2s}'.format(""), end="")
					print(""+Fore.WHITE, end="")
				else:	
					print ('{:>4s}'.format(str(mat[i][j]))+'{:>2s}'.format(""), end="")

			print ("")
	else:
		print("P%d = [ "%x, end="")
		for j in range(len(mat)):
			print ('{:>4s}'.format(str(mat[j]))+'{:>2s}'.format(""), end="")
			if j< (len(mat)-1):
				print(" , ", end="")
		print(" ]")
	print(Fore.WHITE+"")
		
def leerMat(matriz, X):
	if X==-1:
		for i in range(len(matriz)):
			for j in range(len(matriz)):
				matriz[i][j] = float(input("Elemento %d %d : " %(i,j)))
	else:
		printMat(matriz, -1, -1, X)
		for j in range(len(matriz)):
			matriz[X][j] = float(input("Elemento %d %d : " %(X,j)))

	return matriz

def pPV(mat, X, Y, n):
	z=0.01
	aux=0.0
	if n==1 :
		z=pNormal(1, mat, X, Y, n)
	else:
		z=pNormal(1,mat, X, Y, n)
		for i in range(1, n):
			z=z-(pPV(mat, X, Y, i)*pNormal(1, mat, Y, Y, n-i))

	return z

def validacion(matriz):
	suma=0
	for k in range(len(matriz)):
		suma=0
		for l in range(len(matriz)):
			suma=suma+matriz[k][l]
		if suma!=1 :
			leerMat(matriz, k)

def datDeProb(n, inicio, objetivo, pasos):
	inicio=n+1
	while inicio>=n or inicio<=-1:
		inicio = int(input("Estado Inicial (i): "))
		if inicio>=n or inicio<=-1:
			print(Fore.RED+"", end="")
			print("El estado inicial debe ser mayor o igual a 0 y menor a %d.\nIntenelo de nuevo.\n" %n)
			print(""+Fore.WHITE, end="")
		else:
			break

	objetivo=n+3
	while objetivo>=n or objetivo<=-1:
		objetivo = int(input("Estado Final (j): "))
		if objetivo>=n or objetivo<=-1 :
			print(Fore.RED+"", end="")
			print("El estado final debe ser ser mayor o igual a 0 y menor a %d.\nIntenelo de nuevo.\n" %n)
			print(""+Fore.WHITE, end="")
		else:
			break
	pasos=-1
	while pasos<=-1:
		pasos = int(input("Número De Periodos (n): "))
		if pasos<=-1:
			print(Fore.RED+"", end="")
			print("El número de Periodos debe ser mayor o igual a 0.\nIntentelo de nuevo.\n")
			print(""+Fore.WHITE, end="")			

	aux=(inicio, objetivo, pasos)
	return aux

def pNormal(Op, matriz, inicio, objetivo, pasos):
	n=len(matriz)
	arreglo = np.zeros(n)
	arreglo[inicio]=1	
	nuevo = arreglo
	
	nuevo2=[]
	for i in range(n):
		if i!=objetivo:
			nuevo2.append(0)
		else:
			nuevo2.append(1)
	
	for i in range(pasos):
	    nuevo2 = np.matmul(nuevo,matriz)
	    nuevo = nuevo2

	prob=nuevo2[objetivo]
	return prob

def matVect():
	init()
	n=1
	while n<=1:
		n = int(input("Introduce el número de estados: "))
		if n<=1 :
			print(Fore.RED+"", end="")
			print("El número de estados debe ser mayor o igual a 2.\nIntentelo de nuevo.\n")
			print(""+Fore.WHITE, end="")
		else:
			break

	print("")
	matriz = []
	for i in range(n):
		matriz.append([0]*n)

	matriz=leerMat(matriz, -1)
	validacion(matriz)
	
	Op=1
	inicio=0
	objetivo=0
	pasos=0
	while Op==1:
		printMat(matriz, -1, 0, 0)
		print("")
		aux=datDeProb(n, inicio, objetivo, pasos)
		inicio=aux[0]
		objetivo=aux[1]
		pasos=aux[2]

		print("\n\nLa probabilidad de primera vez es: ")
		prob=pPV(matriz, inicio, objetivo, pasos)
		print("P"+str(inicio)+"(T"+str(objetivo)+" = "+str(pasos)+") = "+Fore.GREEN+str(prob)+"\n"+Fore.WHITE)

		Op=float(input("\n¿Desea Calcular otra probabilidad?\n1.-Si.\nIngrese otro número para salir.\n"))


matVect()

# A continuación de pone el Link del programa:
# https://drive.google.com/file/d/1vGXc7VB-HkPTfPzOABc5HiFxhrcjHvpW/view?usp=sharing
