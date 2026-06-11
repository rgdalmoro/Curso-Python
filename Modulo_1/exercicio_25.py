#Exercício Python 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
#https://www.youtube.com/watch?v=WHWGz2Dy1ZU&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=36

nome=str(input('Digite o nome completo> ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))