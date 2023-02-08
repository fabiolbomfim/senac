#Você deve criar com Python uma lista para armazenar esses resultados
#(e outros resultados que quiser no mesmo formato, o código precisa
#funcionar para qualquer lista que seja inserida nesse formato) e depois
#uma função que busca o candidato de acordo com os critérios
#digitados pelo usuário. O usuário vai informar qual a nota mínima de e,
#t, p e s que ele deseja buscar, nossa aplicação deve listar quem são os
#candidatos disponíveis com nota maior ou igual a essas informadas
#pelo usuário.
#⇨ Ao buscar por alguém com resultados 4,4,8,8 por exemplo vamos
#receber que os candidatos 1 e 5 atendem esse critério, foram bem no
#teste prático e apresentaram um ótimo nível de soft skills!



lista = [] 
while True:
    nome = input('Nome do candidato: ')
    nota1 = float(input('Digite a nota da entrevista: '))
    nota2 = float(input('Digite a nota do teste teorico: ')) 
    nota3 = float(input('Digite a nota teste pratico: ')) 
    nota4 = float(input('Digite a nota do softskill: '))
    
    candidatos={nome,nota1,nota2,nota3,nota4}

    lista_candidato = [nome, nota1, nota2,nota3,nota4]
    lista.append(lista_candidato)
    cont = input('Quer continuar? [S/N] ').strip().upper()[0]
    if cont == 'N':
        break
      
print('-'*70) 
print('-=' *5,' LISTA COM NOMES E NOTAS DOS CANDIDATOS ','-='*5) 
print('-'*70)
print(f'{"NOME":^15} {"EX":>12} {"TX":>10} {"PX":>9} {"SX":>9}')
print('-'*70)
for pos,n in enumerate(lista):
    print(f'{pos+1} > {n[0]:<15}{+n[1]:>10}{n[2]:>10}{n[3]:>10}{n[4]:>10}') 
    #print("Candidato""_"+str()+"e"+str(nota1)+"_"+"t"+str(nota2)+"_"+"p"+str(nota3)+"_"+"s"+str(nota4))
print('-'*70)

def busca():
    return
p = int(input('Mostrar notas de qual Candidato? [00 para encerrar] '))
#p = str (input("E,T,P,S [00 para encerrar]"))
if p == 00:
    print('Encerrando...')
    print('-=' *5,' Finalizado ','-='*5)     
if len(lista) >= p > 0:
        print(len(lista), p) 
        print(f'{lista[p-1][0]} tirou notas {lista[p-1][1]},{lista[p-1][2]},{lista[p-1][3]},{lista[p-1][4]}')
else:
    print('  candidato não encontrado  ') 




    
