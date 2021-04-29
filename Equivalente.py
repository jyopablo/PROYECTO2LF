from graphviz import Digraph
import os 

def crear():
	os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
	dot = Digraph(comment='The Round Table')

	dot.node('A', 'King Arthur')
	dot.node('B', 'Sir Bedevere the Wise')
	dot.node('L', 'Sir Lancelot the Brave')

	dot.edges(['AB', 'AL'])
	dot.edge('B', 'L', constraint='false')

	dot.render('tests/test.jpg', view=True) 