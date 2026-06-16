#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
#https://www.youtube.com/watch?v=4vFCzKuHOn4&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=42

#HEAD

titulo='Verificador de Par ou Ímpar'
print('\n')
print('+-'*(len(titulo)//2))
print(titulo)
print('+-'*(len(titulo)//2))
print('\n')
#MAIN
n=int(input('Digite um número inteiro: '))
if n%2==0:
    print('\nNúmero Par')
else:
    print('\nNúmero Ímpar')

