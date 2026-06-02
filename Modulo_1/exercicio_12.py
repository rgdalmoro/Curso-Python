#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
#https://www.youtube.com/watch?v=4MAmKOT9FeU&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=20

titulo='CALCULADORA DE DESCONTO'

print('='*len(titulo))
print(titulo)
print('='*len(titulo))

valor=float(input('Digite o valor do produto: R$'))
desconto=float(input('Digite o desconto em %:'))

print('\nCom o desconto de {:.1f}%, o produto reduz R${:.2f} reais e fica R${:.2f} reais.'.format(desconto,(desconto/100)*valor,valor-((desconto/100)*valor)))