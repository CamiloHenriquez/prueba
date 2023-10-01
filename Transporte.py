class Transporte:
    def __init__(self, tipo, peso):
        self.__tipo = tipo
        self.__peso = peso

    def calcular_despacho(self):
        pass

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso