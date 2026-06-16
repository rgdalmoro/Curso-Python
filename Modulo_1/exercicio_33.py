#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
#https://www.youtube.com/watch?v=a_8FbW5oH6I&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=45

a=int(input('Digite o primeiro valor: '))
b=int(input('Digite o segundo valor: '))
c=int(input('Digite o terceiro valor: '))
maior=a
menor=c

if a>b:
    if b>c:
        maior=a
        menor=c
    else:
        if a>c:
            maior=a
            menor=b
        else:
            maior=c
            menor=b
else:
    if b>c:        
        if a>c:
            maior=b
            menor=c
        else:
            maior=b
            menor=a
    else:
        maior=c
        menor=a
    
    print('O maior número é {}.'.format(maior))

    print('O menor número é {}.'.format(menor))