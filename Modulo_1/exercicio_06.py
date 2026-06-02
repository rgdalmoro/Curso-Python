#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
#https://www.youtube.com/watch?v=mqcNw_dhl8I&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=14

n=int(input("Digite um número:"))
print("O número digitado é {}, seu dobro é {}, triplo é {} e raiz quadrada é {:.0f}.".format(n,n*2,n*3,n**0.5))