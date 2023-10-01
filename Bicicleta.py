from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self, aro, peso, precio, marca):
        super().__init__("Bicicleta", peso)
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def cotizar(self):
        pass

    def get_aro(self):
        return self.__aro

    def set_aro(self, aro):
        self.__aro = aro

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio
    
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca
