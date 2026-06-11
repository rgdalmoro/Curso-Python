#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
#https://www.youtube.com/watch?v=EQQt-6QqXOs&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=33

nome=str(input("Digite o nome completo: ")).strip()
print('O nome completo em maisculas é: {}.'.format(nome.upper()))
print('O nome completo em minusculas é: {}.'.format(nome.lower()))
print('O nome contem {} letras.'.format(len(nome)-nome.count(' ')))
print('O primeiro nome tem {} letras.'.format(len(nome.split()[0])))
