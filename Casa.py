from Residencia import Residencia

class Casa(Residencia):

    def __init__(self, idImovel, nomeProprietario, numeroQuartos, numeroVagasGaragem, precoAreaConstruida, numeroPavimentos, areaPavimento, areaLivre, precoAreaLivre):
        super().__init__(idImovel, nomeProprietario, numeroQuartos, numeroVagasGaragem, precoAreaConstruida)
        self.__numeroPavimentos = numeroPavimentos
        self.__areaPavimento = areaPavimento
        self.__areaLivre = areaLivre
        self.__precoAreaLivre = precoAreaLivre

    # Metodo implementado da superclasse Imovel
    def preco(self):
        return (self.getPrecoAreaConstruida() * self.__areaPavimento * self.__numeroPavimentos) + (self.__precoAreaLivre * self.__areaLivre)

    def areaConstruida(self):
        return self.__areaPavimento * self.__numeroPavimentos

    def getNumeroPavimentos(self):
        return self.__numeroPavimentos

    def getAreaPavimento(self):
        return self.__areaPavimento

    def getAreaLivre(self):
        return self.__areaLivre

    def getPrecoAreaLivre(self):
        return self.__precoAreaLivre