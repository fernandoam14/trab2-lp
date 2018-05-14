from Imovel import Imovel

class Residencia(Imovel):

    def __init__(self, idImovel, nomeProprietario, numeroQuartos, numeroVagasGaragem, precoAreaConstruida):
        super().__init__(idImovel, nomeProprietario)
        self.__numeroQuartos = numeroQuartos
        self.__numeroVagasGaragem = numeroVagasGaragem
        self.__precoAreaConstruida = precoAreaConstruida

    # Metodo da superclasse Imovel a ser implementado pelas subclasses
    def preco(self):
        raise NotImplementedError

    def getNumeroQuartos(self):
        return self.__numeroQuartos

    def getNumeroVagasGaragem(self):
        return self.__numeroVagasGaragem

    def getPrecoAreaConstruida(self):
        return self.__precoAreaConstruida