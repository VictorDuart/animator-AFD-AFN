from graphviz import Digraph        #para instalar: $ pip install graphviz
import os
import sys

#funções para quebrar linhas do arquivo de entrada
def getPrimeiraParte(primeiraParte):
    estadosPrimeiraParte = primeiraParte.split(" ")
    return estadosPrimeiraParte

def getSegundaParte(segundaParte):
    segundaParte = segundaParte.rstrip("\n")
    estadosSegundaParte = segundaParte.split(" ")
    return estadosSegundaParte

def contaLinha(docname):    
    with open(docname) as doc:
        i = 0
        for line in doc:
            i += 1
        return i

AF = open(sys.argv[1], 'r', encoding="utf8")

dot = Digraph(comment='AF')
dot.attr('node', shape='circle')
dot.attr('edge', color='black')
dot.attr(rankdir='LR', size='8,5')

tamanhoDoc = contaLinha(sys.argv[1])
i = 0

#A configuração dos autômatos será mapeada em lista de dicionários.
Trans = dict()                                      #cada transição será um dicionário
listaTrans = list()                                 #lista que conterá todas as transições 

#for para quebrar o txt e obter os dados
for line in AF:
    if i == 0:                                      #primeira linha (estados inicias ; estados finais)
        primeiraLinha = line.split(" ; ")
        primeiraParte = str(primeiraLinha[0])
        segundaParte = str(primeiraLinha[1])
        estadosIniciais = getPrimeiraParte(primeiraParte)
        estadosFinais = getSegundaParte(segundaParte)
    else:                                           #linhas que contém as transições
        if (i < (tamanhoDoc - 1)):
            linhasTrans = line.split(" > ")
            primeiraParte = str(linhasTrans[0])
            segundaParte = str(linhasTrans[1])
            chave = getPrimeiraParte(primeiraParte)
            valor = getSegundaParte(segundaParte)
            Trans = {'estadoAtual': chave[0], 'transicao': chave[1], 'estadoFinal': valor[0]}
            listaTrans.append(Trans)
        else:                                      #ultima linha (palavra)
            if(i == (tamanhoDoc - 1)):
                linhaPalavra = line.split(" : ")
                palavra = linhaPalavra[1]
    i+=1

#gerar automato inicial
for inicial in estadosIniciais:         
    dot.node('ponto', 'ponto', shape = 'point')
    dot.node (inicial, inicial, style='filled', fillcolor='grey', shape='circle')
    dot.edge('ponto', inicial, shape='circle')

for final in estadosFinais:
    dot.node(final, final, shape='doublecircle')

for trans in listaTrans:
    dot.node(trans['estadoAtual'], trans['estadoAtual'])
    dot.node(trans['estadoFinal'], trans['estadoFinal'])
    dot.edge(trans['estadoAtual'], trans['estadoFinal'], label=trans['transicao'])
    
dot.render('output/grafo0.gv', view=False, format='png')           

for inicial in estadosIniciais:
    dot.node (inicial, inicial, style='filled', fillcolor='white')

estadoCorrente = estadosIniciais
contaPalavra = 0
f = 1                                               #auxilar para gerar as imagens
auxiliar = list()

#realizar o passo a passo para cada palavra
for letra in palavra:
    for trans in listaTrans:
        if(trans['estadoAtual'] in estadoCorrente):
            if(letra == trans['transicao'] or trans['transicao'] == '/'):
                
                auxiliar.append(trans['estadoFinal']) 

                if(trans['estadoAtual'] not in auxiliar):
                    dot.node(trans['estadoAtual'], trans['estadoAtual'], style='filled', fillcolor='white')
                
                dot.node(trans['estadoFinal'], trans['estadoFinal'], style='filled', fillcolor='grey')
            
                if(trans['estadoFinal'] in estadosFinais and contaPalavra == (len(palavra)-1)):
                    dot.node(trans['estadoFinal'], trans['estadoFinal'], style='filled', fillcolor = 'green')
            
                if(trans['estadoFinal'] not in estadosFinais and contaPalavra == (len(palavra)-1)):
                    dot.node(trans['estadoFinal'], trans['estadoFinal'], style='filled', fillcolor = 'red')
 
    flag = 0 
    dot.render('output/grafo'+str(f)+'.gv', view=False, format='png')

    for estado in auxiliar:
        dot.node(estado, estado, style='filled', fillcolor='white')
    
    if(len(auxiliar)!=0):
        estadoCorrente = auxiliar.copy()
        auxiliar.clear()
        
    f+=1
    contaPalavra += 1

print(f'Palavra: {palavra}')

script = 'convert -delay 50 -loop 0 output/*.png output/animacao.gif'

os.system(script)

AF.close
