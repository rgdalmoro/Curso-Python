#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
#https://www.youtube.com/watch?v=PGqHyzWoagc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=43

#HEAD

titulo='Calculadora de Valor da Passagem'
print('\n')
print('-+'*(len(titulo)//2))
print(titulo)
print('-+'*(len(titulo)//2))
print('\n')
print('Valor por km até 200km: R$0,50')
print('Valor por km acima de 200km: R0,45')
print('-'*len(titulo))

#MAIN

km=int(input('Digite a qte de km da viagem: '))
if km<200:
    print('\nPara {}km, será cobrado R$0,50 por km, num total de R$ {:.2f}.\n'.format(km,km*0.50))
else:
    print('\nSerá cobrado R$0,45 pelos primeiros 200 km, num subtotal de R$ 90.00')
    print('\nPara {}km restantes será cobrado R$0,45 por km, num subtotal de R$ {:.2f}.'.format(km-200,(km-200)*0.45))
    print('\nO total a ser pago é R$ {:.2f}.\n'.format(90+(km-200)*0.45))