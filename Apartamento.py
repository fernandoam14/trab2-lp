from Residencia import Residencia

class Apartamento(Residencia):

    def __init__(self, idImovel, nomeProprietario, numeroQuartos, numeroVagasGaragem, precoAreaConstruida, idAndar, areaConstruida, possuiAreaLazer, numeroAndares):
        super().__init__(idImovel, nomeProprietario, numeroQuartos, numeroVagasGaragem, precoAreaConstruida)
        self.__idAndar = int(idAndar)
        self.__areaConstruida = float(areaConstruida)
        self.__possuiAreaLazer = possuiAreaLazer
        self.__numeroAndares = int(numeroAndares)

    # Metodo implementado da superclasse Imovel
    def preco(self):
        if self.__possuiAreaLazer == 'S':
            return self.getPrecoAreaConstruida() * self.__areaConstruida * (0.9 + (self.__idAndar / self.__numeroAndares)) * 1.15
        else:
            return self.getPrecoAreaConstruida() * self.__areaConstruida * (0.9 + (self.__idAndar / self.__numeroAndares)) * 1

    def getIdAndar(self):
        return self.__idAndar

    def getAreaConstruida(self):
        return self.__areaConstruida

    def getPossuiAreaLazer(self):
        return self.__possuiAreaLazer

    def getNumeroAndares(self):
        return self.__numeroAndares