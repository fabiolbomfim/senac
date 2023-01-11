#Resolva o problema abaixo:
#Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo
#(M/F) e 
# salário. 
# Faça um algoritmo que leia esses dados coletados e informe:

#a) a média de salário do grupo;
#b) maior e menor idade do grupo;
#c) quantidade de mulheres com salário até R$1000,00.
# ● Encerre a entrada de dados quando for digitada uma idade negativa.

s = ''

while (s != 'não'):
    idade1 = int(input('Digite a idade da primeira pessoa: '))
    idade2 = int(input('Digite a idade da segunda pessoa: '))
    idade3 = int(input('Digite a idade da terceira pessoa: '))
    print('')
    sexo1 = input('Digite o sexo da primeira pessoa: ')
    sexo2 = input('Digite o sexo da segunda pessoa: ')
    sexo3 = input('Digite o sexo da terceira pessoa: ')
    print('')
    salario1 = float(input('Digite o sálario da primeira pessoa: '))
    salario2 = float(input('Digite o salário da segunda pessoa: '))
    salario3 = float(input('Digite o salário da terceira pessoa: '))
    print('')
    media_salario = (salario1 + salario2 + salario3)/3
    print ('A média salárial é: R$ %6.2f' % media_salario)
    print ('A menor idade dos entrevistados é:',min(idade1, idade2, idade3))
    print ('E a maior idade é:',max(idade1, idade2, idade3))
    s = input('Deseja continuar? ')