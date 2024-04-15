""" Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo."""

num1 = int(input("Insira um número inteiro "))
num2 = int(input("Insira um número inteiro "))
num3 = float(input("Insira um número real "))

produto = (2*num1) + (num2/2)
soma = (3*num1) + num3
cubo = num3**3

print(produto)
print(soma)
print(cubo)