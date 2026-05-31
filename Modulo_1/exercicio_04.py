#Exercicio 04
#https://www.youtube.com/watch?v=tHYxjJxtJko&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=12
entrada=input('Digite algo:')
print('O tipo primitivo desta entrada é {}'.format(type(entrada)))
print('Só tem espaços:', entrada.isspace())
print('É número: {}'.format(entrada.isnumeric()))
print('É alfanumérico: {}'.format(entrada.isalnum()))
print('É alfabético: {}'.format(entrada.isalpha()))
print('Está em minúsculas: {}'.format(entrada.islower()))
print("Está em maiusculas:{}".format(entrada.isupper()))
print("Está capitalizado: {}".format(entrada.istitle()))