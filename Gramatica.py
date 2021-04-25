import os 
from CargarArchivo import *
def analizar(opcion):
	os.system("cls")
	for i in range(0,100):
		print("")
	tamaño=len(Cantidad1)
	for i in range(0,tamaño):
		igual=opcion==Cantidad1[i]
		if igual==True:
		     print('Nombre de la gramtica: '+Titulos[i])
		     print('No terminales: '+Noterminales[i])
		     print('Terminales: '+Terminales[i])
		     print('Terminal Inicial: '+Terminalinicial[i])

	tamaño2=len(Cantidad3)
	for i in range(0,tamaño2):
		igual=opcion==Cantidad3[i]
		if igual==True:
		     print('Produccion: '+Produccion[i])


