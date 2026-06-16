#Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#https://www.youtube.com/watch?v=cyGY_83m4Xw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=44

#HEAD
import time
titulo='Verificador de Ano Bissexto'
print('\n')
print('-'*len(titulo))
print(titulo)
print('-'*len(titulo))

#MAIN

ano=int(input('Digite o ano em 4 dígitos / Digite 0 para ano corrente:'))

if ano==0:
   if int(time.strftime("%Y"))%4==0:
     print('O ano de {} é BISSEXTO.'.format(time.strftime("%Y")))
   else:
     print('O ano de {} NÃO é BISSEXTO.'.format(time.strftime("%Y")))
else:
  if ano%4==0:
    print('O ano de {} é BISSEXTO.'.format(ano))
  else:
     print('O ano de {} NÃO é BISSEXTO.'.format(ano))


#GABARITO / OTIMIZADO E TBEM PARA REGRA ANOS CENTARIOS NÃO DIVISIVEIS POR 400

print('\nGABARITO\n')

if ano==0:
  ano=int(time.strftime("%Y"))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('O ano de {} é BISSEXTO.'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO.'.format(ano))
  








