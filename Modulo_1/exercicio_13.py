#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
#https://www.youtube.com/watch?v=cTkivN8XcJ0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=21

titulo='CALCULO DE REAJUSTE SALARIAL'
print('=+'*(len(titulo)//2))
print(titulo)
print('=+'*(len(titulo)//2))

salario=float(input('Digite o salario atual: R$'))
reajuste=float(input('Digite o reajuste em %:'))
print('O novo salario, com reajuste de {:.1f}% será de R${:.2f} reais'.format(reajuste,salario+(salario*(reajuste/100))))