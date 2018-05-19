from Imovel import Imovel
from Residencia import Residencia
from Terreno import Terreno
from Casa import Casa
from Apartamento import Apartamento
from TerrenoTriangular import TerrenoTriangular
from TerrenoRetangular import TerrenoRetangular
from TerrenoTrapezoidal import TerrenoTrapezoidal

# Funcao que escreve os arquivo de saida saida.txt e result.txt
#
# Entrada:
# catalogo de imoveis lidos nos arquivos de entrada
# tupla com os dados especificados lidos a serem levados em consideracao na escrita
#
# Saida:
# -
def escreveSaida(catalogo, dados):
    arq = open('saida.txt', 'w')
    i = escreveItemA(arq, catalogo, dados[0], dados[4])
    j = escreveItemB(arq, catalogo, dados[1], dados[5])
    k = escreveItemC(arq, catalogo, dados[2], dados[3], dados[6])
    arq.close()
    escreveResult(i, j, k)

# Funcao que escreve o arquivo de saida result.txt
#
# Entrada:
# id do imovel na i-esima posicao da lista ordenada do item A
# id do terreno argiloso na j-esima posicao da lista ordenada do item B
# id da casa na k-esima posicao da lista ordenada do item C
#
# Saida:
# -
def escreveResult(i, j, k):
    arq = open('result.txt', 'w')
    arq.write(str(i + j + k))
    arq.close()

# Funcao que escreve no arquivo saida.txt os valores pedidos no item A
#
# Entrada:
# arquivo onde a escrita sera feita
# catalogo de imoveis
# percentual de imoveis caros a serem escritos
# indice i do imovel a ser escolhido da lista ordenada, que sera utilizado para a escrita do arquivo result.txt
#
# Saida:
# o id do imovel na i-esima posicao da lista ordenada
def escreveItemA(arq, catalogo, percentualImoveisCaros, i):
    n = len(catalogo)
    numeroImoveis = (percentualImoveisCaros * n) // 100 # Quantidade de imoveis a serem considerados na lista
    catalogo.sort(key = lambda x: (x.preco(), x.getIdImovel())) # Ordenacao do catalogo em ordem crescente de preco
    listaImoveis = catalogo[(n - numeroImoveis):]   # Lista apenas com a quantidade de imoveis a serem considerados
    for imovel in listaImoveis:
        arq.write(str(imovel.getIdImovel()))    # Escrita do id de cada imovel da lista
        if imovel != listaImoveis[-1]:
            arq.write(', ')
    arq.write('\n')
    if i > 0 and i <= numeroImoveis:
        return (listaImoveis[i - 1]).getIdImovel()  # Retorna o id do i-esimo imovel da lista, caso i valido
    else:
        return 0

# Funcao que escreve no arquivo saida.txt os valores pedidos no item B
#
# Entrada:
# arquivo onde a escrita sera feita
# catalogo de imoveis
# percentual de menores terrenos argilosos a serem escritos
# indice j do terreno argiloso a ser escolhido da lista ordenada, que sera utilizado para a escrita do arquivo result.txt
#
# Saida:
# o id do terreno argiloso na j-esima posicao da lista ordenada
def escreveItemB(arq, catalogo, percentualMenoresArgilosos, j):
    catalogo = [x for x in catalogo if (isinstance(x, Terreno) and (x.getTipoSolo() == 'G'))]   # Considera o catalogo apenas com terrenos argilosos
    n = len(catalogo)
    numeroArgilosos = (percentualMenoresArgilosos * n) // 100   # Quantidade de terrenos argilosos a serem considerados na lista
    catalogo.sort(key = lambda x: (x.area(), x.getIdImovel()), reverse = True)  # Ordenacao do catalogo em ordem decrescente de area
    listaArgilosos = catalogo[(n - numeroArgilosos):]   # Lista apenas com a quantidade de terrenos argilosos a serem considerados
    for argiloso in listaArgilosos:
        arq.write(str(argiloso.getIdImovel()))  # Escrita do id de cada terreno argiloso da lista
        if argiloso != listaArgilosos[-1]:
            arq.write(', ')
    arq.write('\n')
    if j > 0 and j <= numeroArgilosos:
        return (listaArgilosos[j - 1]).getIdImovel()    # Retorna o id do j-esimo terreno argiloso da lista, caso j valido
    else:
        return 0

# Funcao que escreve no arquivo saida.txt os valores pedidos no item C
#
# Entrada:
# arquivo onde a escrita sera feita
# catalogo de imoveis
# area limite para a escrita
# preco limite para a escrita
# indice k da casa a ser escolhida da lista ordenada, que sera utilizado para a escrita do arquivo result.txt
#
# Saida:
# o id da casa na j-esima posicao da lista ordenada
def escreveItemC(arq, catalogo, areaLimite, precoLimite, k):
    catalogo = [x for x in catalogo if (isinstance(x, Casa) and (x.areaConstruida() > areaLimite) and (x.preco() < precoLimite))]   # Considera o catalogo apenas com casas dentro de um limite especificado de area e preco
    n = len(catalogo)
    catalogo.sort(key = lambda x: (x.getNumeroQuartos(), x.getIdImovel()), reverse = True)  # Ordenacao do catalogo em ordem decrescente de numero de quartos
    for casa in catalogo:
        arq.write(str(casa.getIdImovel()))  # Escrita do id de cada casa da lista
        if casa != catalogo[-1]:
            arq.write(', ')
    arq.write('\n')
    if k > 0 and k <= n:
        return (catalogo[k - 1]).getIdImovel()  # Retorna o id da k-esima casa da lista, caso k valido
    else:
        return 0