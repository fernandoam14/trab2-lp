class Imovel:

    def __init__(self, idImovel, nomeProprietario):
        self.__idImovel = int(idImovel)
        self.__nomeProprietario = nomeProprietario

    # Metodo a ser implementado pelas subclasses
    def preco(self):
        raise NotImplementedError

    def getIdImovel(self):
        return self.__idImovel

    def getNomeProprietario(self):
        return self.__nomeProprietario