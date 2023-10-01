from Tecnologia import Tecnologia

class Consola(Tecnologia):
    def __init__(self,marca,voltaje,precio,eficiencia,nombre_consola,version):
        super().__init__(marca,voltaje,precio,eficiencia)
        self.__nombre_consola = nombre_consola
        self.__version = version

    def calcular_descuentos(self):

        if super().get_eficiencia() in ['A','B']:
            descuento_eficiencia = 0.5
        elif super().get_eficiencia() in ['C','D']:
            descuento_eficiencia = 0.3
        elif super().get_eficiencia() in ['E','F']:
            descuento_eficiencia = 0.1
        else:
            descuento_eficiencia = 0

        if self.__version in "Lite":
            descuento_total = descuento_eficiencia + 0.05
        else:
            descuento_total = descuento_eficiencia
        
        total = super().get_precio() - (super().get_precio() * descuento_total)
        return f"Marca: {super().get_marca()}\nVoltaje: {super().get_voltaje()}\nPrecio: ${super().get_precio()}\nEficiencia: {super().get_eficiencia()}\nNombre consola: {self.__nombre_consola}\nVersion: {self.__version}\nDescuento: {descuento_total * 100}%\nPrecio total: ${total}"

        
    def get_nombre_consola(self):
        return self.__nombre_consola

    def set_nombre_consola(self, nombre_consola):
        self.__nombre_consola = nombre_consola

    def get_version(self):
        return self.__version

    def set_version(self, version):
        self.__version = version