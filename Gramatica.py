import os 
from CargarArchivo import *
g_nombre=""
g_Terminales=""
g_Noterminales=""
g_TerminalInicial=""
Iteracion=[]
Pila=[]
Entrada=[]
Transiciones=[]
def analizar(opcion):
	imprimir(opcion)
	AutomataPila(opcion)	     


def AutomataPila(opcion):
	global g_Terminales
	global g_Noterminales
	global g_TerminalInicial
	siguiente=""
	cajon=""
	x1="ï"
	x2="λ"
	x3="λ"
	x4="p"
	x5="#"
	a="a"
	palabra1=""
	palabra2=""
	palabra3=""
	contadorIter=0
	Iteracion.append(contadorIter)
	Pila.append(" ")
	Entrada.append(a)
	Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+x5+")")
	x1="p"
	x4="q"
	contadorIter += 1
	Iteracion.append(contadorIter)
	Pila.append(x5)
	Entrada.append(a)
	Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+g_TerminalInicial+")")	
	tamaño2=len(Cantidad3)
	for i in range(0,tamaño2):
		igual=opcion==Cantidad3[i]
		if igual==True:
			paso1=True
			paso2=False
			paso3=False
			paso4=False
			contadorterminales=0
			contadornoterminales=0
			Texto=Produccion[i]
			for k in Texto:
				caracter=k
				if paso1==True:
					if caracter==":":
						paso1=False
						paso2=True
					else:
						pass
				elif paso2==True:
					if caracter==">":
						x4="q"
						x1="q"
						x3=palabra1
						paso2=False
						paso3=True
					elif caracter=="-":	
						pass
					else:
						if caracter==" ":
							pass
						else:
						    palabra1=palabra1+caracter
				elif paso3==True:
					ter=caracter in g_Terminales
					noter=caracter in g_Noterminales
					if ter==True:
						palabra2=palabra2+caracter
						contadorterminales += 1
						if contadorterminales==2:
							siguiente=caracter
					elif noter==True:
						palabra2=palabra2+caracter
						contadornoterminales += 1	

			if contadorterminales==2  and contadornoterminales==1:
				ultimo=palabra2
				contadorIter += 1
				Iteracion.append(contadorIter)
				Pila.append(palabra1+cajon)
				Entrada.append(a)
				Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+palabra2+")")
				conversion(palabra2,siguiente,a,contadorIter,x1,x2,x3,x4,cajon)
				cajon=siguiente+cajon
				palabra1=""
				palabra2=""

			if contadorterminales==1 and contadornoterminales==0:
				if siguiente != None:
					ultimo=palabra2
					contadorIter += 1
					Iteracion.append(contadorIter)
					Pila.append(palabra1+cajon)
					Entrada.append(a)
					Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+palabra2+")")
					palabra1=""
					palabra2=""
				else:
				    contadorIter += 1
				    Iteracion.append(contadorIter)
				    Pila.append(palabra1+cajon)
				    Entrada.append(a)
				    Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+palabra2+")")
				    ultimo=palabra2
				    palabra1=""
				    palabra2=""

			if contadorterminales==0 and contadornoterminales==1:
				if siguiente != None:
					ultimo=palabra2
					contadorIter += 1
					Iteracion.append(contadorIter)
					Pila.append(palabra1+cajon)
					Entrada.append(a)
					Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+palabra2+")")
					palabra1=""
					palabra2=""
				else:
				    contadorIter += 1
				    Iteracion.append(contadorIter)
				    Pila.append(palabra1+cajon)
				    Entrada.append(a)
				    Transiciones.append("("+x1+","+x2+","+x3+","+x4+","+palabra2+")")
				    ultimo=palabra2
				    palabra1=""
				    palabra2=""


			if contadorterminales==1 and contadornoterminales==1:
				palabra1=""
				palabra2=""
				pass

	cajon=ultimo+cajon
	if cajon != None:
		for i in cajon:
			contadorIter += 1
			Iteracion.append(contadorIter)
			Pila.append(cajon)
			Entrada.append(a)
			Transiciones.append("(q,"+i+","+i+",q,"+x2+")")
	print(Iteracion)		
	print(Pila)		 
	print(Transiciones)		


def imprimir(opcion):
	global g_Terminales
	global g_Noterminales
	global g_TerminalInicial
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
		    g_nombre=Titulos[i]
		    g_Noterminales=Noterminales[i]
		    g_Terminales=Terminales[i]
		    g_TerminalInicial=Terminalinicial[i]

	tamaño2=len(Cantidad3)
	for i in range(0,tamaño2):
		igual=opcion==Cantidad3[i]
		if igual==True:
		     print('Produccion: '+Produccion[i])

def conversion(palabra1,siguiente,a,contadorIter,x1,x2,x3,x4,cajon):
	contadorIter += 1
	Iteracion.append(contadorIter)
	Pila.append(palabra1+cajon)
	Entrada.append(a)
	Transiciones.append("("+x1+","+siguiente+","+siguiente+","+x4+","+x2+")")
