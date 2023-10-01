from Transporte import Transporte

class Bicicleta(Transporte):
    def __init__(self,aro,peso, precio, marca,tipo='Bicicleta'):
        super().__init__('Bicicleta', peso)
        self.__aro = aro
        self.__peso = peso
        self.__precio = precio
        self.__marca = marca

    def calcular_despacho(self):
        costo_base_despacho = 4000
        if super().get_tipo() == "Scooter": 
            costo_total = costo_base_despacho + (300 * self.__peso)
        elif super().get_tipo() == "Bicicleta":
            costo_total = costo_base_despacho + (400 * self.__peso)
        else:
            costo_total = costo_base_despacho
        return f'Tipo: {super().get_tipo()}\nAro: {self.__aro}\nPeso: {self.__peso}\nPrecio: {self.__precio}\nMarca: {self.__marca}\nCosto despacho: {costo_total}'

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
