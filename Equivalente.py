from graphviz import Digraph
from graphviz import Graph
from CargarArchivo import *
from Gramatica import *
import os 

def crear(opcion):
	cadena=""
	os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
	g = Digraph('finite_state_machine',format='png')
	g.attr(rankdir='LR', size='8,5')
	g.node('i', shape='circle', width='1')
	g.node('p', shape='circle', width='1')
	g.node('q', shape='circle', width='2')
	g.node('f', shape='doublecircle', width='1')
	g.edge('i','p', label='λ,λ;#', width='1')
	tamaño=len(Cantidad1)
	for i in range(0,tamaño):
		igual=opcion==Cantidad1[i]
		if igual==True:
		    TerInicial="λ,λ;"+Terminalinicial[i]
		    Titulo=Titulos[i]	    
	g.edge('p','q', label=TerInicial, width='1')

	for i in TransicionesGrafico:
		cadena=cadena+i+"\n"

	g.edge('q','q',label=cadena, width='1')

	g.edge('q','f', label='λ,#;λ', width='1')

	g.render('Graficos/AP_'+Titulo.replace("\n",""),view=False)
	crearhtlm(opcion)

def crearhtlm(opcion):
	tamaño=len(Cantidad1)
	for i in range(0,tamaño):
		igual=opcion==Cantidad1[i]
		if igual==True:
		    Titulo=Titulos[i]
		    terminales=Terminales[i]
		    alfabeto=Terminales[i]+","+Noterminales[i]+",#"
	crear=open("Graficos_AP_"+Titulo.replace("\n","")+".html","w")
	crear.write("<html lang=\"es\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Document</title><link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6\" crossorigin=\"anonymous\"><style>body{background-color:powderblue;}</style></head><body><di class=\"container-fluid\"><div class=\"m-0 vh-100 row justify-content-center align-items-center\"><div class=\"Card border border\" style=\"width: 50rem\"><img src=\"Graficos\AP_"+Titulo+".png\" class=\"card-img-top\" alt=\"Automata Pila\"><div class=\"card-body\">")
	crear.write("<h1>Nombre:AP_"+Titulo+"</h1>")
	crear.write("<h4>Terminales={"+terminales+"}</h4>")
	crear.write("<h4>Alfabeto de pila={"+alfabeto+"}</h4>")
	crear.write("<h4>Estados={ i,p,q,f}</h4>")
	crear.write("<h4>Estado inicial={i}</h4>")
	crear.write("<h4>Estado de aceptacion={f}</h4>")
	crear.write("</div></div></div></di></body></html>")
	crear.close()
	os.system("Graficos_AP_"+Titulo.replace("\n","")+".html")	    

