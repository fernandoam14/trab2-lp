from Leitura import leCatalogo, leAtual, leEspec
from Escrita import escreveSaida

catalogo = leCatalogo()
catalogo = leAtual(catalogo)
dados = leEspec()
escreveSaida(catalogo, dados)