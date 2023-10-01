class Tecnologia:

    def __init__(self,voltaje,precio,eficiencia,marca):
    
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        self.__marca = marca

    def calcular_descuento(self):
        if self.__eficiencia == 'A' or 'B':
            return 0.5
        elif self.__eficiencia == 'C' or 'D':
            return 0.3
        elif self.__eficiencia == 'E' or 'F':
            return 0.1
        else:
            return 0

    def cotizar(self):
        pass

    def get_voltaje(self):
        return self.__voltaje

    def set_voltaje(self, voltaje):
        self.__voltaje = voltaje

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def get_eficiencia(self):
        return self.__eficiencia

    def set_eficiencia(self, eficiencia):
        self.__eficiencia = eficiencia

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca
