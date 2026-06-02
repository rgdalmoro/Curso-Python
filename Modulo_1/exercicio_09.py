#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
#https://www.youtube.com/watch?v=qajq3SI0QQs&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=17

n=int(input('Digite um valor:'))
print('-'*30)
print('{:2}  x {:2} =  {}'.format(1,n,n*1))
print('{:2}  x {:2} =  {}'.format(2,n,n*2))
print('{:2}  x {:2} =  {}'.format(3,n,n*3))
print('{:2}  x {:2} =  {}'.format(4,n,n*4))
print('{:2}  x {:2} =  {}'.format(5,n,n*5))
print('{:2}  x {:2} =  {}'.format(6,n,n*6))
print('{:2}  x {:2} =  {}'.format(7,n,n*7))
print('{:2}  x {:2} =  {}'.format(8,n,n*8))
print('{:2}  x {:2} =  {}'.format(9,n,n*9))
print('{:2}  x {:2} =  {}\n'.format(10,n,n*10))