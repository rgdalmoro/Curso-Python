#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#https://www.youtube.com/watch?v=QroT8cZMRnc&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=35

cidade=str(input('Digite o nome de uma cidade: ')).strip()
print(cidade.split()[0].lower()=='santo')