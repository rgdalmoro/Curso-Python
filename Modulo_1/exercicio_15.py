#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
#https://www.youtube.com/watch?v=I4NYUeetLAc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=23


##CABEÇALHO

titulo='Calculadora de Aluguel de Carros'
barra='+-'*(len(titulo)//2)

print(barra)
print(titulo)
print(barra)

##MAIN

dias=int(input('Digite o número de dias:'))
km=int(input('Digite o número de km rodados:'))
print("\nO valor a pagar para {} dias e {} km rodados será de R$ {:.2f}".format(dias,km,60*dias+0.15*km))




