#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
#https://www.youtube.com/watch?v=-iSbDpl5Jhw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=26

from math import trunc
n=float(input('Digite um valor:'))
print('A porção inteira de {} é {}.'.format(n,trunc(n)))
