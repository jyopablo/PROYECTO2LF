from Gramatica import *
from CargarArchivo import *
import os
def crear(opcion):
	tamaño=len(Cantidad1)
	for i in range(0,tamaño):
		igual=opcion==Cantidad1[i]
		if igual==True:
		    Titulo=Titulos[i]
	crear=open("AP_"+Titulo.replace("\n","")+".html","w")
	crear.write("<html lang=\"es\">")
	crear.write("<head><meta charset=\"ISO-8859-1\"><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl\" crossorigin=\"anonymous\"><title>AP_"+Titulo+"</title></head><body>")
	crear.write("<div class=\"container\"><div class=\"row justify-content-center\"><div class=\"col-4\"><h1>Tabla AP_"+Titulo+"</h1></div></div>")
	crear.write("<table class=\"table\"><thead><tr class=\"table-dark\"><th scope=\"col\">No</th><th scope=\"col\">Pila</th><th scope=\"col\">Entrada</th><th scope=\"col\">Transiciones</th></tr></thead><tbody>")
	x=len(Transiciones)
	for i in range(0,x):
		crear.write("<tr><th scope=\"row\">"+str(i)+"</th><td>"+Pila[i]+"</td><td>"+Entrada[i]+"</td><td>"+Transiciones[i]+"</td></tr>")
	crear.write("</table></div></body></html>")	
	crear.close()
	os.system("AP_"+Titulo.replace("\n","")+".html")