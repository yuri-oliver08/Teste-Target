#Questão 05

"""
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
"""

print("Digite o texto que deseja ver invertido!")
txt = str(input())

def inverterString(texto):
	return texto[::-1]

print("Aqui está seu texto invertido!")
print(inverterString(txt))