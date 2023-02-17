#CONTEXTO
#Uma empresa de recrutamento recebeu muitos currículos
#para determinadas vagas e agora precisa classificar
#quantos candidatos tem o perfil necessário e quantos
#candidatos estão concorrendo a cada vaga específica.

#O QUE É PARA FAZER?

#Desenvolver um projeto (usando dicionários) que vai gravar
#a quantidade de currículos para aquela vaga e quantas
#pessoas têm as palavras-chave necessárias no currículo.
#Para isso, nosso código Python vai checar para qual vaga a
#pessoa se inscreveu e o resumo que a pessoa enviou em busca dessas informações.

#As palavras-chave das vagas são:
#◼ Vaga 1: Python, Programação, Desenvolvimento;
#◼ Vaga 2: Análise de dados, Dados, SQL
#⇨ Nosso código deve ficar pedindo para qual vaga a pessoa se inscreveu e o resumo de
#cada participante em loop (só deve parar quando inserir o número 0 na pergunta da vaga).

#⇨ O texto do resumo/minibio vai ser informado pelo usuário (como desafio extra você
#pode tentar ler esse texto de arquivos txt em uma pasta e eliminar essa etapa de pedir
#os textos em loop)
# e então vamos checar se temos as palavras-chave necessárias e
#marcar como um candidato válido para a vaga.

#No final do código (quando o usuário digitar 0 para sair) vamos mostrar os totais,
#quantas pessoas estão inscritas em cada vaga e quantas tem o resumo/minibio com as
#palavras que estamos buscando.


nome=[]
inscriçoes={}
vaga=[]
vagas=[] #
resumo={}# guarda o texto do resumo profissional
vagas = {
    1: {"nome": "Vaga 1", "palavras_chave": ["python", "programação", "desenvolvimento"]},
    2: {"nome": "Vaga 2", "palavras_chave": ["análise de dados", "dados", "sql"]}
       }# dicionario com os dados necessarios para verificacao de vagas
nome = input( "Digite o seu nome: ")
resumo = input("Insira seu resumo profissional: ")
inscricoes = {vaga: {"total": 0, "validos": 0} for vaga in vagas}
def checar_palavras_chave(texto, palavras_chave):
    return any(palavra in texto.lower() for palavra in palavras_chave)

while True:
    vaga = int(input(f" se inscreveu para vaga 1:python, programação , desenvolvimento ?\n                   vaga 2: análise de dados, dados, sql ? \n      (digite 0 para sair): "))
    if vaga == 0:
        break
    if vaga not in vagas:
        print("Vaga inválida. Tente novamente.")
        continue
    inscricoes[vaga]["total"] += 1
    
    if checar_palavras_chave(resumo, vagas[vaga]["palavras_chave"]): # checa a palavar chave para compatibilidade com a vaga escolhida
        inscricoes[vaga]["validos"] += 1
    for vaga, dados in inscricoes.items():# retorna os itens para verificacao dos dados validados com a vaga
        print('_'*100)
        print(f"{vagas[vaga]['nome']}: {dados['total']} inscrições, {dados['validos']} com as palavras-chave correspondente a vaga .")
       # o cadidato corresponde ou nao a vaga ofertada 
   

        #with open("minibio.txt","r+")as resumo: 
        #   for minibio in resumo:
        #     print(minibio) 