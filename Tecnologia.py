class Tecnologia:

    def __init__(self,marca,voltaje,precio,eficiencia):
        
        self.__marca = marca
        self.__voltaje = voltaje
        self.__precio = precio
        self.__eficiencia = eficiencia
        

    def calcular_descuento(self):
        if self.__eficiencia in ['A','B']:
            descuento_eficiencia = 0.5
        elif self.__eficiencia in ['C','D']:
            descuento_eficiencia = 0.3
        elif self.__eficiencia in ['E','F']:
            descuento_eficiencia = 0.1
        else:
            descuento_eficiencia = 0
        
        total = self.__precio - (self.__precio * descuento_eficiencia)
        return f"Marca: {self.__marca}\nVoltaje: {self.__voltaje}\nPrecio: ${self.__precio}\nEficiencia: {self.__eficiencia}\nDescuento por eficiencia: {descuento_eficiencia * 100}%\nPrecio total: ${total}"

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
