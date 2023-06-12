#Crie uma função que recebe um ângulo em radianos e retorna o ângulo correspondente em graus arredondados para uma casa decimal.
#O número π pode ser carregado do módulo math com from math import pi.

import math

def radians_to_degrees(rad):
	return round(math.degrees(rad), 1)