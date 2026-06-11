#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#https://www.youtube.com/watch?v=_Nk02-mfB5I&list=PLHz_AreHm4dm6wYOIW20Nyg12TAjmMGT-&index=20
import random
n1=str(input("Digite o nome do aluno 1: "))
n2=str(input('Digite o nome do aluno 2: '))
n3=str(input('Digite o nome do aluno 3: '))
n4=str(input('Digite o nome do aluno 4: '))
lista=[n1,n2,n3,n4]
print('\nO aluno escolhido é {}.\n'.format(random.choice(lista)))