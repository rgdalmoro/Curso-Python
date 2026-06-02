#Exercício Python 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
#https://www.youtube.com/watch?v=_QfISzy0IKs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=15

n1=float(input('Digite a nota do primeiro aluno:'))
n2=float(input('Digite a nota do segundo aluno:'))
print("A nota dos alunos foram {} e {}, e a média é {:.1f}".format(n1,n2,(n1+n2)/2))