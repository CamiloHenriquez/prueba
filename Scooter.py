from Transporte import Transporte
from Tecnologia import Tecnologia

class Scooter(Tecnologia,Transporte):
    def __init__(self,peso,marca,voltaje,precio,eficiencia,aro,velocidad,tipo='Scooter'):   
    
        Tecnologia.__init__(self,marca,voltaje,precio,eficiencia)
        Transporte.__init__(self,'Scooter',peso) 
        self.__aro = aro
        self.__velocidad = velocidad
        self.__peso = peso
        

    def calcular_despacho(self):
        costo_base_despacho = 4000
        if super().get_tipo() == "Scooter": 
            costo_total_despacho = costo_base_despacho + (300 * super().get_peso())
        elif super().get_tipo() == "Bicicleta":
            costo_total_despacho = costo_base_despacho + (400 * super().get_peso())
        else:
            costo_total_despacho = costo_base_despacho

        if super().get_eficiencia() in ['A','B']:
            descuento_eficiencia = 0.5
        elif super().get_eficiencia() in ['C','D']:
            descuento_eficiencia = 0.3
        elif super().get_eficiencia() in ['E','F']:
            descuento_eficiencia = 0.1
        else:
            descuento_eficiencia = 0
        
        
        descuento = super().get_precio() - (super().get_precio() * descuento_eficiencia)
        
        total = descuento + costo_total_despacho
        
        return f'Marca: {super().get_marca()}\nVoltaje: {super().get_voltaje()}\nPrecio: ${super().get_precio()}\nEficiencia: {super().get_eficiencia()}\nAro: {self.__aro}\nVelocidad: {self.__velocidad}\nPeso: {super().get_peso()}\nDescuento: {descuento_eficiencia * 100}%\nCosto despacho: {costo_total_despacho}\nPrecio total: ${total}'