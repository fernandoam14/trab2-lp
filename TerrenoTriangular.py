from Terreno import Terreno

class TerrenoTriangular(Terreno):

    def __init__(self, idImovel, nomeProprietario, tipoSolo, precoTerreno, base, altura):
        super().__init__(idImovel, nomeProprietario, tipoSolo, precoTerreno)
        self.__base = base
        self.__altura = altura

    # Metodo implementado da superclasse Terreno
    def area(self):
        return (self.__base * self.__altura) / 2

    def getBase(self):
        return self.__base

    def getAltura(self):
        return self.__altura