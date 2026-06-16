#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
#https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=47

a=float(input('Digite o primeiro valor: '))
b=float(input('Digite o segundo valor: '))
c=float(input('Digite o terceiro valor: '))
maior=a
meio=b
menor=c

if a>b:
    if b>c:
        maior=a
        meio=b
        menor=c
    else:
        if a>c:
            maior=a
            menor=b
            meio=c
        else:
            maior=c
            menor=b
            meio=a
else:
    if b>c:        
        if a>c:
            maior=b
            menor=c
            meio=a
        else:
            maior=b
            menor=a
            meio=c
    else:
        maior=c
        menor=a
        meio=b
    
print('Regra: soma de dois segmentos tem que ser maior que o terceiro segmento!')
if meio+menor>maior:
    print('Temos um triangulo!')
else:
    print('NÃO temos um triangulo!')