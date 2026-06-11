#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
#https://www.youtube.com/watch?v=9GvsphwW26k&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=29

##HEAD
import math

titulo='Calculadora de Principais Medidas Trigonométricas'
barra='+-'*(len(titulo)//2)

print(barra)
print(titulo)
print(barra)


#MAIN

ang=int(input('Digite o ângulo: '))
print('O seno de {} é {:.2f}.'.format(ang,math.sin(math.radians(ang))))
print('O cosseno de {} é {:.2f}.'.format(ang,math.cos(math.radians(ang))) )
print('A tangente de {} é {:.2f}.'.format(ang,math.tan(math.radians(ang))))