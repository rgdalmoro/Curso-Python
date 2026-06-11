#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#https://www.youtube.com/watch?v=SifYYsXhLM8&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=38

nome=str(input('Digite o nome completo: ')).strip()
print('O primeiro nome é: {}.'.format(nome.split()[0].capitalize()))
print('O último nome é: {}.'.format(nome[nome.rfind(' ')+1:].capitalize()))
