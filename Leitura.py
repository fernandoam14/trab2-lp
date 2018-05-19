from Imovel import Imovel
from Residencia import Residencia
from Terreno import Terreno
from Casa import Casa
from Apartamento import Apartamento
from TerrenoTriangular import TerrenoTriangular
from TerrenoRetangular import TerrenoRetangular
from TerrenoTrapezoidal import TerrenoTrapezoidal

# Funcao que le o arquivo de entrada catalogo.txt
# Entrada:
# -
#
# Saida:
# catalogo de imoveis com todos os imoveis inseridos
def leCatalogo():
    arq = open('catalogo.txt', 'r')
    leitura = arq.read()    # Le o arquivo e armazena todo o conteudo em forma de string
    if leitura == '':   # Caso o arquivo esteja vazio
        arq.close()
        return []
    else:   # Caso o arquivo nao esteja vazio
        leitura = leitura.split('\n\n')  # Quebra a string em uma lista de blocos, em que cada bloco contem os dados de um imovel
        catalogo = []
        for bloco in leitura:
            bloco = bloco.splitlines()  # Quebra cada bloco em uma lista, em que cada elemento eh uma linha do bloco
            catalogo = insereImovelNoCatalogo(bloco, catalogo)  # Insere o imovel no catalogo, dadas as suas informacoes
        arq.close()
        return catalogo

# Funcao que le o arquivo de entrada atual.txt
# Entrada:
# catalogo de imoveis a ser atualizado
#
# Saida:
# catalogo de imoveis com as atualizacoes feitas
def leAtual(catalogo):
    arq = open('atual.txt', 'r')
    leitura = arq.read()    # Le o arquivo e armazena todo o conteudo em forma de string
    if leitura == '':    # Caso o arquivo esteja vazio
        arq.close()
        return catalogo
    else:   # Caso o arquivo nao esteja vazio
        leitura = leitura.split('\n\n') # Quebra a string em uma lista de blocos, em que cada bloco contem os dados de um imovel
        for bloco in leitura:
            bloco = bloco.splitlines()  # Quebra cada bloco em uma lista, em que cada elemento eh uma linha do bloco
            if bloco[0] == 'i': # Caso a acao a ser feita seja uma insercao
                catalogo = insereImovelNoCatalogo(bloco[1:], catalogo)  # Insere o imovel no catalogo, dadas as suas informacoes
            elif bloco[0] == 'a':   # Caso a acao a ser feita seja uma atualizacao
                for imovel in catalogo:
                    if imovel.getIdImovel() == int(bloco[2]):
                        catalogo.remove(imovel) # Remove o imovel requerido do catalogo
                        break
                catalogo = insereImovelNoCatalogo(bloco[1:], catalogo)  # Reinsere o imovel requerido no catalogo, com suas novas informacoes
            else:   # Caso a acao a ser feita seja uma remocao
                for imovel in catalogo:
                    if imovel.getIdImovel() == int(bloco[1]):
                        catalogo.remove(imovel) # Remove o imovel requerido do catalogo
                        break
        arq.close()
        return catalogo

# Funcao que le o arquivo de entrada espec.txt
#
# Entrada:
# -
#
# Saida:
# tupla com os dados especificados lidos, da forma:
#   (percentualImoveisCaros, percentualMenoresArgilosos, areaLimite, precoLimite, i, j, k)
def leEspec():
    arq = open('espec.txt', 'r')
    leitura = arq.read().splitlines()   # Le o arquivo e armazena suas linhas em uma lista
    dados = ()
    for linha in leitura:
        dados += (int(linha),)  # Insere os dados de cada linha lida em uma tupla
    return dados

# Funcao que insere um imovel no catalogo, dadas as suas informacoes em um bloco lido de um arquivo
#
# Entrada:
# bloco com as informacoes do imovel
# catalogo de imoveis em que o imovel sera inserido
#
# Saida:
# catalogo atualizado com o novo imovel inserido
def insereImovelNoCatalogo(bloco, catalogo):
    if bloco[0] == 'casa':
        catalogo.append(Casa(bloco[1], bloco[2], bloco[3], bloco[4], bloco[7], bloco[5], bloco[6], bloco[8], bloco[9]))
    elif bloco[0] == 'apto':
        catalogo.append(Apartamento(bloco[1], bloco[2], bloco[3], bloco[4], bloco[7], bloco[5], bloco[6], bloco[8], bloco[9]))
    elif bloco[0] == 'triang':
        catalogo.append(TerrenoTriangular(bloco[1], bloco[2], bloco[3], bloco[4], bloco[5], bloco[6]))
    elif bloco[0] == 'retang':
        catalogo.append(TerrenoRetangular(bloco[1], bloco[2], bloco[3], bloco[4], bloco[5], bloco[6]))
    else:
        catalogo.append(TerrenoTrapezoidal(bloco[1], bloco[2], bloco[3], bloco[4], bloco[5], bloco[6], bloco[7]))
    return catalogo