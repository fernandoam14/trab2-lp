from Imovel import Imovel

class Terreno(Imovel):

    def __init__(self, idImovel, nomeProprietario, tipoSolo, precoTerreno):
        super().__init__(idImovel, nomeProprietario)
        self.__tipoSolo = tipoSolo
        self.__precoTerreno = precoTerreno

    # Metodo implementado da superclasse Imovel
    def preco(self):
        if self.__tipoSolo == 'A':
            return self.__precoTerreno * self.area() * 0.9
        elif self.__tipoSolo == 'G':
            return self.__precoTerreno * self.area() * 1.3
        else:
            return self.__precoTerreno * self.area() * 1.1

    # Metodo a ser implementado pelas subclasses
    def area(self):
        raise NotImplementedError

    def getTipoSolo(self):
        return self.__tipoSolo

    def getPrecoTerreno(self):
        return self.__precoTerreno