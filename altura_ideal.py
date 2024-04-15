"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7 """

altura = float(input("Insira sua altura "))
sexo = int(input("Digite 1 se for mulher e 2 se for homem "))
if sexo == 1:
  peso_ideal = (62.1*altura) - 44.7
  print("O seu peso ideal é ", peso_ideal)
elif sexo == 2:
  peso_ideal = (72.7*altura) - 58
  print("O seu peso ideal é ", peso_ideal)
else:
  print("Número inválido")