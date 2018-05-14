from Terreno import Terreno

class TerrenoRetangular(Terreno):

    def __init__(self, idImovel, nomeProprietario, tipoSolo, precoTerreno, lado1, lado2):
        super().__init__(idImovel, nomeProprietario, tipoSolo, precoTerreno)
        self.__lado1 = lado1
        self.__lado2 = lado2

    # Metodo implementado da superclasse Terreno
    def area(self):
        return self.__lado1 * self.__lado2

    def getLado1(self):
        return self.__lado1

    def getLado2(self):
        return self.__lado2