#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#https://www.youtube.com/watch?v=xM4AX3Lp2mo&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=18

din=float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} reais você pode comprar U$${:.2f} dolares'.format(din,din/5.50))