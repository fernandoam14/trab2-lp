from Leitura import leCatalogo, leAtual, leEspec
from Escrita import escreveSaida
#from Casa import Casa
#from Apartamento import Apartamento
#from Imovel import Imovel
#from Residencia import Residencia
#from Terreno import Terreno

catalogo = leCatalogo()
catalogo = leAtual(catalogo)
dados = leEspec()
escreveSaida(catalogo, dados)

#for each in catalogo:
#    print(each.getIdImovel())
#print(len(catalogo))
#print(dados)

#c = Casa(10,1,3,4,5,6,7,8,9)
#if isinstance(c, Residencia):
#    print(':D')
#if isinstance(c, Imovel):
#    print(':D')
#
#a = Apartamento(10,2,3,4,5,6,7,8,9)
#teste = [a, c]
#print(teste)
#
#print(teste)