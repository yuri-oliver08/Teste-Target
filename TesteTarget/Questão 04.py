#Questão 04

"""
Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""
valorSP = 67.83643
valorRJ = 36.67866
valorMG = 29.22988
valorES = 27.16548
valorOU = 19.84953

total = valorES + valorMG + valorOU + valorRJ + valorSP
def porcentagem(valor):
	percentual = 100 * float(valor)/float(total)
	percentualF = "{:.2f}".format(percentual)
	return str(percentualF) + "%"

print("Porcentagem de representação dos estados dentro do valor total mensal da distribuidora:\n")
print("O percentual de representação do estado de São Paulo (SP) foi:",porcentagem(valorSP))
print("O percentual de representação do estado de Rio de Janeiro (RJ) foi:",porcentagem(valorRJ))
print("O percentual de representação do estado de Minas Gerais (MG) foi:",porcentagem(valorMG))
print("O percentual de representação do estado de Espírito Santos (ES) foi:",porcentagem(valorES))
print("O percentual de representação de outros estados foi:",porcentagem(valorOU))