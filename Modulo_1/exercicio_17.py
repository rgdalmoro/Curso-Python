#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
#https://www.youtube.com/watch?v=vmPW9iWsYkY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=27

from math import hypot
cat1=float(input('Digite o cateto adjacente: '))
cat2=float(input('Digite o cateto oposto: '))
print('A hipotenusa para os catetos de valores {} e {} é {.2f}.'.format(cat1,cat2,hypot(cat1,cat2)))