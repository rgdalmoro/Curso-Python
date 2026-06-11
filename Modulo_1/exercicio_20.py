#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#https://www.youtube.com/watch?v=OPh0nngbBSY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=30
import random
n1=str(input("Digite o nome do aluno 1: "))
n2=str(input('Digite o nome do aluno 2: '))
n3=str(input('Digite o nome do aluno 3: '))
n4=str(input('Digite o nome do aluno 4: '))
lista=[n1,n2,n3,n4]
random.shuffle(lista)
print('\nA nova ordem dos alunos é: {}.\n'.format((lista)))