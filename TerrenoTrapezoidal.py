from Terreno import Terreno

class TerrenoTrapezoidal(Terreno):

    def __init__(self, idImovel, nomeProprietario, tipoSolo, precoTerreno, base1, base2, altura):
        super().__init__(idImovel, nomeProprietario, tipoSolo, precoTerreno)
        self.__base1 = float(base1)
        self.__base2 = float(base2)
        self.__altura = float(altura)

    # Metodo implementado da superclasse Terreno
    def area(self):
        return ((self.__base1 + self.__base2) * self.__altura) / 2

    def getBase1(self):
        return self.__base1

    def getBase2(self):
        return self.__base2

    def getAltura(self):
        return self.__altura