from Leitura import *

catalogo = leCatalogo()
catalogo = leAtual(catalogo)
dados = leEspec()

for each in catalogo:
    print(each.getIdImovel())
print(len(catalogo))
print(dados)