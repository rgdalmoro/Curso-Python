#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
#https://www.youtube.com/watch?v=mzSJpn9ldt4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=19

titulo = "CALCULADORA DE NECESSIDADE DE TINTA"
print("=" * len(titulo))
print(titulo)
print("=" * len(titulo))


larg=float(input('\nDigite a largura da parede em metros:'))
alt=float(input('\nDigite a altura da parede em metros:'))
print('\nEssa parede tem {:.2f} m de largura e {:.2f} m de altura, com uma área de {:.2f} m2.\n'.format(larg,alt,larg*alt))
print('Você vai precisar de {:.1f} litros de tinta para pintar essa parede.\n\n'.format(larg*alt/2))