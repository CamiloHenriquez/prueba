class Transporte:
    def __init__(self, tipo, peso):
        self.__tipo = tipo
        self.__peso = peso

    def calcular_despacho(self):

        costo_base_despacho = 4000
        if self.__tipo == "Scooter": 
            costo_total = costo_base_despacho + (300 * self.__peso)
        elif self.__tipo == "Bicicleta":
            costo_total = costo_base_despacho + (400 * self.__peso)
        else:
            costo_total = costo_base_despacho
        return costo_total

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        self.__tipo = tipo

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        self.__peso = peso