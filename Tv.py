from Tecnologia import Tecnologia

class Tv(Tecnologia):
    def __init__(self,marca,voltaje,precio,eficiencia,tamaño):
        super().__init__(marca, voltaje, eficiencia, precio)
        self.__tamaño = tamaño

    def cotizar(self):
        pass

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self, tamaño):
        self.__tamaño = tamaño