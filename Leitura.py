from Imovel import Imovel
from Residencia import Residencia
from Terreno import Terreno
from Casa import Casa
from Apartamento import Apartamento
from TerrenoTriangular import TerrenoTriangular
from TerrenoRetangular import TerrenoRetangular
from TerrenoTrapezoidal import TerrenoTrapezoidal

def leCatalogo():
    arq = open('catalogo.txt', 'r')
    leitura = arq.read().split('\n\n')
    catalogo = []
    for bloco in leitura:
        bloco = bloco.splitlines()
        catalogo = insereImovelNoCatalogo(bloco, catalogo)
    arq.close()
    return catalogo

def leAtual(catalogo):
    arq = open('atual.txt', 'r')
    leitura = arq.read().split('\n\n')
    for bloco in leitura:
        bloco = bloco.splitlines()
        if bloco[0] == 'i':
            catalogo = insereImovelNoCatalogo(bloco[1:], catalogo)
        elif bloco[0] == 'a':
            for imovel in catalogo:
                if imovel.getIdImovel() == int(bloco[2]):
                    catalogo.remove(imovel)
                    break
            catalogo = insereImovelNoCatalogo(bloco[1:], catalogo)
        else:
            for imovel in catalogo:
                if imovel.getIdImovel() == int(bloco[1]):
                    catalogo.remove(imovel)
                    break
    arq.close()
    return catalogo

def leEspec():
    arq = open('espec.txt', 'r')
    leitura = arq.read().splitlines()
    dados = ()
    for linha in leitura:
        dados += (int(linha),)
    return dados

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