#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=22

titulo='Conversor de Temperaturas'
print('+-'*(len(titulo)//2))
print(titulo)
print('+-'*(len(titulo)//2))

celsius=float(input('Digite a temperatura em graus Celsius: '))
print(" A temperatura de {} C representa {} F.".format(celsius,(celsius*1.8)+32))
