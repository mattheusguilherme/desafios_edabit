#Dado o raio de um círculo e a área de um quadrado, retorne True se a circunferência do círculo for maior que o perímetro do quadrado e False se o perímetro do quadrado for maior que a circunferência do círculo.
#Você pode usar Pi com 2 casas decimais (3.14).
#A circunferência de um círculo é igual a 2 * Pi * raio.
#Para encontrar o perímetro de um quadrado usando sua área, encontre a raiz quadrada da área (para obter o comprimento do lado) e multiplique por 4.

from math import pi
def circle_or_square(rad, area):
    return 2 * pi * rad > 4 * pow(area, 0.5) 