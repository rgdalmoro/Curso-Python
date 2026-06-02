#Exercício Python 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
#https://www.youtube.com/watch?v=KjcdG05EAZc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=16
n=int(input("Digite a medida em metros:"))
print('O valor equivalente de {} m é de:\n {} km\n {} dm\n {} cm\n {} mm'.format(n,n/1000,n*10,n*100,n*1000))