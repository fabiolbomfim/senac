#Projeto fale comigo
# Senac Resilia Curso Formacao de Analise de dados: 

#integrantes Fabio , Victor, Flavia, Fernanda

#Ramo da empresa Exame de imagem

# usuario informa o nome e cpf
#escolhe 3 opcoes de sobre as susas duvidas 
# 1 Exame
# 2 Agendamento
# 3 falar com atendente

from time import sleep 
cadastros = [] 
cadastro = [] 
cont = "1" 
hr =[['dia 20 - 10 horas'],['dia 21- 14 horas'],['dia 22 - 18 horas']] 
atendimento=[[1],[2],[3],[4],[5,]] 
select=" "
opcao = 0
print ("\n\n Olá somos A IMAGEM Medicina Diagnostica.\n Nosso atendente virtual vai fazer algumas perguntas.\n")
nome = str(input ("Por favor informe o seu nome para iniciar o atendimento:\n"))
list.append(cadastro,nome) 

print ("Agora preciso que informe o seu CPF")
cpf = int(input ("digite apenas os numeros do seu cpf:\n"))
list.append(cadastro,cpf) 
print("_"*60)
print('\n1 - Duvidas sobre agendamento de exames ?:\n2 - Duvidas sobre o seu agendamento ? \n3 - Para falar coma atendente: \n') 
opcao = int(input('digite o numero para continuar \n'))

while (cont=="1"): 
  
  if (opcao == 1): 
    print(   "Duvidas sobre agendamentos de exames:\n agendamento pelo site www.imagemdiagnosticos.com.br/agenda;\n agendamento pelo whatsapp 21-91234-5678;\n agendamento pelo telefone 21-3333-2222;\n agendamento na unidade rua x, numero: y, bairro:z ") 
    select = "Exames" 
    list.append(cadastro,select)

  if (opcao == 2):
    print("O seu exame de ultrassom do abdomem total está marcado dia 31/01 às 9h da manhã na unidade de Botafogo, chegar com 30 min de antecedência.")
    select = " procedimento de exam "
    list.append(cadastro,select)

  if (opcao == 3):
    print("Aguarde que estamos transferindo para um dos nossos atendentes, peço que aguarde")
    sleep(5)
    print("num de nossos atendentes fara conta no numero cadastrado.")
    select = "atendente "
    list.append(cadastro,select)
  print('-'*60)
  break
  #cont = input('Deseja continuar?
  
print ("\n Gostaria de marcar outro exame ?\n\n1 - para marcar ultrassonografia: \n2 - para marcar ressonância magnética:\n3 - para marcar tomografia:\n4 - voltar ao menu anterior. \n5 - Sair.\n")

opcao = int(input('digite o numero para continuar \n'))
while opcao ==4:
    if (opcao == 1):
        print("voce escolheu ultrassonografia")
        select = 'ultrassom'
        list.append(cadastro, select)

    if (opcao == 2):
        print("voce escolheu ressonância magnética")
        select = 'Ressonancia'
        list.append(cadastro, select)

    if (opcao == 3):
        print("voce escolheu tomografia")
        select = 'tomografia'
        list.append(cadastro, select)
        
        print("\nAguarde alguns segundos estamos consultando a nossa agenda")
        sleep(2)
    if (opcao == 4):
        opcao = int(input('digite o numero \n'))
                
    break
print("Para o exame solicitado temos as seguintes datas ")
print("\n1 - dia 20 - 10 horas: \n2 - dia 21- 14 horas: \n3 - dia 22 - 18 horas:")

opcao = int(input('digite o numero para continuar \n'))

if (opcao == 1):
    print(hr[0])

elif (opcao == 2):
    print(hr[1])

else:       
    print("dia 22 - 18 horas")
    print('-'*60)
list.append(cadastros, cadastro)

print('\n os dados cadastrados sao:\n')
print(cadastro) 
def imprime (lista): #"""le e imprime cada linha""" 

 for i in lista: print(i)
 print("\n")

print("atendimento finalizado")

#** PRA VC CHAMAR A FUNÇÃO E PRINTAR CADA LINHA DE CADASTRO E HORA MARCADA VC VAI CHAMAR TIPO "imprime(cadastros)" **
#*** TEM QUE COLOCAR O LIST.APPEND PRA SALVAR A HORA NA LISTA DO CADASTRO (SE VC QUISER), AI VC TERIA QUE COLOCAR POR EX. LIST.APPEND(CADASTRO,HR[1]) PRA SALVAR A HORA DEPOIS - E ISSO DENTRO DO IF, ELIF E ELSE.
# NÃO ESQUECE DE UMA MENSAGEM DE DESPEDIDA KKKK E É BOM COLOCAR A DESPEDIDA FORA DO WHILE, QUE APARECE MESMO SE A PESSOA DIGITAR UMA OPÇÃO ERRADA*
#INCLUIR TEXTO DE CONFIRMACAO 
# NÃO ESQUECE TBM KKKK)
#-> SE VC QUISER FAZER O LOOPING PRA FICAR VOLTANDO PRO INICIO NO WHILE, VC VAI TER QUE TIRAR O BREAK E ATUALIZAR A VARIAVEL "CONT" NO LUGAR DELE, TIPO: cont = input('Deseja continuar? "barra n" 1 - sim "barra n" 2 - não
#QUALQUER VALOR DIFERENTE DE 1 VAI DAR O BREAK AUTOMATICAMENTE
