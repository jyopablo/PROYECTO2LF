from tabulate import tabulate
import sys
from tkinter import filedialog
import CargarArchivo as CargarArchivo
import Gramatica as Gramatica
import html_tabla as html_tabla
import Equivalente as Equivalente
from CargarArchivo import *
from Gramatica import *
import time
import os
DatosCargados="______________Datos Cargados Correctamente_______________"
ruta=""
opcion=0
def Inicio():
	table = [["SUPER AUTOMATA"],["JUAN PABLO GONZALEZ LEAL"],["201901374"]]
	print(tabulate(table, tablefmt="pretty"))
	conteo(6)


def conteo(valor):
	for i in range(valor):
		time.sleep(1)
		valor -= 1
		print(valor,end="    ")
		if valor==0:
			print('')
			menu()

def menu():
	global ruta
	global opcion
	while True:
		print('1. Cargar archivo')
		print('2. Mostrar informacion de la gramatica')
		print('3. Generar automata de pila equivalente')
		print('4. reporte de recorrido')
		print('5. Reporte en tabla')
		print('6. Salir')
		valor=int(input('ELIGE UNA OPCION'))
		if valor == 1:
			eliminar()
			ruta=filedialog.askopenfilename(title="abrir")
			archivo=open(ruta)
			for linea in archivo.readlines():
				CargarArchivo.analizar(linea)
				archivo.close()
			print(DatosCargados)
			menu()
		elif valor == 2:
			tamaño=len(Titulos)
			for i in range(0,tamaño):
				print(str(Cantidad1[i])+". Nombre:"+Titulos[i])

			opcion=int(input('ELIJA UNA OPCION'))
			Gramatica.analizar(opcion)
			esperar()
		elif valor == 3:
			Equivalente.crear(opcion)
			menu()
		elif  valor == 4:
			print('posicion 4')
			menu()
		elif valor == 5:
			html_tabla.crear(opcion)
			menu()
		elif valor == 6:
			break

def esperar():
	print('1. Desea Mostrar Menu')
	print('2. Desea Salir del Progrma')
	opcion=int(input('ELIJA UNA OPCION'))
	if opcion==1:
		for i in range(0,100):
			print("")
		menu()
	else:
		sys.exit()

def eliminar():
	global ruta
	global opcion
	opcion=0
	g_nombre=""
	g_Noterminales=""
	g_Terminales=""
	g_TerminalInicial=""
	Validar=False
	ContadorCantidad=0
	contador=0
	ruta=""
	Terminales.clear()
	Noterminales.clear()
	Terminalinicial.clear()
	Titulos.clear()
	Produccion.clear()
	Cantidad1.clear()
	Cantidad2.clear()
	Cantidad3.clear()
	Iteracion.clear()
	Pila.clear()
	Entrada.clear()
	Transiciones.clear()
	TransicionesGrafico.clear()

Inicio()
