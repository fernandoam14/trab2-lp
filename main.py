from Leitura import leCatalogo, leAtual, leEspec
from Escrita import escreveSaida

# Leitura do arquivo catalogo.txt
catalogo = leCatalogo()

# Leitura do arquivo atual.txt
catalogo = leAtual(catalogo)

# Leitura do arquivo espec.txt
dados = leEspec()

# Escrita dos arquivos saida.txt e result.txt
escreveSaida(catalogo, dados)