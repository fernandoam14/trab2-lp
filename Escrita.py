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
    arq.close()

def escreveItemA(arq, catalogo, percentualImoveisCaros, i):
    n = len(catalogo)
    numeroImoveis = (percentualImoveisCaros * n) // 100
    catalogo.sort(key = lambda x: (x.preco(), x.getIdImovel()))
    for imovel in catalogo[(n - numeroImoveis):]:
        arq.write(str(imovel.getIdImovel()))
        if imovel != catalogo[-1]:
            arq.write(', ')
    arq.write('\n')
    if i > 0 and i <= n:
        return catalogo[i - 1]
    else:
        return 0

def escreveItemB(arq, catalogo, percentualMenoresArgilosos, j):
    catalogo = [x for x in catalogo if (isinstance(x, Terreno) and (x.getTipoSolo() == 'G'))]
    n = len(catalogo)
    numeroArgilosos = (percentualMenoresArgilosos * n) // 100
    catalogo.sort(key = lambda x: (x.area(), x.getIdImovel()), reverse = True)
    for argiloso in catalogo[(n - numeroArgilosos):]:
        arq.write(str(argiloso.getIdImovel()))
        if argiloso != catalogo[-1]:
            arq.write(', ')
    arq.write('\n')
    if j > 0 and j <= n:
        return catalogo[j - 1]
    else:
        return 0