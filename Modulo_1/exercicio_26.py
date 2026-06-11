#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
#https://www.youtube.com/watch?v=23UOVEetNPY&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=37

frase=str(input('Digite uma frase: ')).strip()
print('A letra a aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A letra a aparece a primeira vez na posição {}.'.format(frase.find('a')+1))
print('A letra a aparece a ultima vez na posição {}.'.format(frase.rfind('a')+1))