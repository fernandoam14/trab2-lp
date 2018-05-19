from Imovel import Imovel
from Residencia import Residencia
from Terreno import Terreno
from Casa import Casa
from Apartamento import Apartamento
from TerrenoTriangular import TerrenoTriangular
from TerrenoRetangular import TerrenoRetangular
from TerrenoTrapezoidal import TerrenoTrapezoidal

def escreveSaida(catalogo, dados):
    arq = open('saida.txt', 'w')
    i = escreveItemA(arq, catalogo, dados[0], dados[4])
    j = escreveItemB(arq, catalogo, dados[1], dados[5])
    k = escreveItemC(arq, catalogo, dados[2], dados[3], dados[6])
    arq.close()
    escreveResult(i, j, k)

def escreveItemA(arq, catalogo, percentualImoveisCaros, i):
    n = len(catalogo)
    numeroImoveis = (percentualImoveisCaros * n) // 100
    catalogo.sort(key = lambda x: (x.preco(), x.getIdImovel()))
    listaImoveis = catalogo[(n - numeroImoveis):]
    for imovel in listaImoveis:
        arq.write(str(imovel.getIdImovel()))
        if imovel != listaImoveis[-1]:
            arq.write(', ')
    arq.write('\n')
    if i > 0 and i <= numeroImoveis:
        return (listaImoveis[i - 1]).getIdImovel()
    else:
        return 0

def escreveItemB(arq, catalogo, percentualMenoresArgilosos, j):
    catalogo = [x for x in catalogo if (isinstance(x, Terreno) and (x.getTipoSolo() == 'G'))]
    n = len(catalogo)
    numeroArgilosos = (percentualMenoresArgilosos * n) // 100
    catalogo.sort(key = lambda x: (x.area(), x.getIdImovel()), reverse = True)
    listaArgilosos = catalogo[(n - numeroArgilosos):]
    for argiloso in listaArgilosos:
        arq.write(str(argiloso.getIdImovel()))
        if argiloso != listaArgilosos[-1]:
            arq.write(', ')
    arq.write('\n')
    if j > 0 and j <= numeroArgilosos:
        return (listaArgilosos[j - 1]).getIdImovel()
    else:
        return 0

def escreveItemC(arq, catalogo, areaLimite, precoLimite, k):
    catalogo = [x for x in catalogo if (isinstance(x, Casa) and (x.areaConstruida() > areaLimite) and (x.preco() < precoLimite))]
    n = len(catalogo)
    catalogo.sort(key = lambda x: (x.getNumeroQuartos(), x.getIdImovel()), reverse = True)
    for casa in catalogo:
        arq.write(str(casa.getIdImovel()))
        if casa != catalogo[-1]:
            arq.write(', ')
    arq.write('\n')
    if k > 0 and k <= n:
        return (catalogo[k - 1]).getIdImovel()
    else:
        return 0

def escreveResult(i, j, k):
    arq = open('result.txt', 'w')
    arq.write(str(i + j + k))
    arq.close()