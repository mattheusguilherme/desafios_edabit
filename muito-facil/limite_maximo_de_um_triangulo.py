#Crie uma função que encontre o alcance máximo da terceira aresta de um triângulo, onde os comprimentos dos lados são todos inteiros.

#Dicas:
#(lado1 + lado2) - 1 = alcance máximo da terceira aresta.
#Os comprimentos dos lados do triângulo são inteiros positivos.
#Não se esqueça de retornar o resultado.

def next_edge(side1, side2):
	maximum_range = (int(side1) + int(side2)) - 1
	return maximum_range