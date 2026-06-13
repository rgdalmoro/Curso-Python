#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
#https://www.youtube.com/watch?v=kchC5KLZSZ4&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=40


#HEAD
import random
titulo='Jogo de Adivinha Números'
print('+-'*(len(titulo)//2))
print(titulo)
print('+-'*(len(titulo)//2))

#MAIN

c=random.randint(0,5)
p=int(input('\nTente adivinhar o número do computador, entre 0 e 5: '))

if p>5:
    print('\n Valor inválido! Digite um valor entre 0 e 5.\n')
else:
    if c==p:
        print('\nParabéns, você acertou o número {} do computador!\n'.format(c))
    else:
        print('\nXi, não acertou. O computador pensou {} e você chutou {}.\n'.format(c,p))
