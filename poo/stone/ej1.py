class Vehiculo(object):
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def presentarCoche(self):
        return "Coche de color {}, tiene {} ruedas, velocidad maxima de {} km/h y {} cc".format(self.color, self.ruedas, self.velocidad, self.cilindrada)

a1 = Coche('rojo', 4, 120, 1100)
print(a1.presentarCoche())