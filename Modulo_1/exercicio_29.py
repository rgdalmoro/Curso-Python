#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
# https://www.youtube.com/watch?v=hgJ_ETNGSj8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=41

#HEAD

titulo='RADAR DE VELOCIDADE'
print('+-'*(len(titulo)//2))
print(titulo)
print('+-'*(len(titulo)//2))

#MAIN

v=int(input('\nInforme a velocidade aferida: '))
if v>87:
    print('\nVocê foi multado! O valor da multa é R$ {:.2f}.\n'.format(7*(v-80)))
elif v>80:
    print('\nCuidado! Você ultrapassou o limite em {} km/h, mas foi apenas advertido.\n'.format(v-80))
else:
    print('\nTudo certo, a velocidade limite é 80km/h.\n')