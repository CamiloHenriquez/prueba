from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self,marca,voltaje,precio,eficiencia,tamano):
        super().__init__(marca, voltaje,precio,eficiencia)
        self.__tamano = tamano

    def get_tamano(self):
        return self.__tamano

    def set_tamano(self, tamano):
        self.__tamano = tamano