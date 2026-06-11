#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=34

num=str(input('Digite um número com até quatro algarismos: '))
print('Este número possui {} unidades de milhar.'.format(num[0]))
print('Este número possui {} centenas.'.format(num[1]))
print('Este número possui {} dezenas.'.format(num[2]))
print('Este número possui {} unidades.'.format(num[3]))

#gabarito

n=int(input('Digite um número de 4 digitos: '))
print('M: {}'.format(n//1000%10))
print('C: {}'.format(n//100%10))
print('D: {}'.format(n//10%10))
print('U: {}'.format(n//1%10))

