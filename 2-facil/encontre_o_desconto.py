#Crie uma função que receba dois argumentos: o preço original e a porcentagem de desconto como números inteiros e retorne o preço final após o desconto.
#Sua resposta deve ser arredondada para duas casas decimais.

def dis(price, discount):
	return price * (100 - discount) * 0.01