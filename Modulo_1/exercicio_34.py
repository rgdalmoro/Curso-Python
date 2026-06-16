#Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
#https://www.youtube.com/watch?v=Sfadj_AzKHw&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=46

salario=float(input('Salário atual: R$  '))

if salario>1250:
    print(f'O salário reajustado em 10% é de R$ {salario*1.1:.2f}')
else:
    print(f'O salário reajustado em 15% é de R$ {salario*1.15:.2f}')

