from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self,marca,voltaje,precio,eficiencia,nombre_consola,version):
        super().__init__(marca,voltaje,precio,eficiencia)
        self.__nombre_consola = nombre_consola
        self.__version = version

    def cotizar(self):
        pass

    def get_nombre_consola(self):
        return self.__nombre_consola

    def set_nombre_consola(self, nombre_consola):
        self.__nombre_consola = nombre_consola

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version