class Vehiculo(object):
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def mostrarAtributos(self):
        return {'color':self.color, 'ruedas':self.ruedas}

class Coche(Vehiculo):
    def __init__(self, color, ruedas, vel, cil):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = vel
        self.cilindrada = cil

    def mostrarAtributos(self):
        attrs = {}
        attrs.update(Vehiculo.mostrarAtributos(self))
        attrs.update({'velocidad': self.velocidad, 'cilindrada':self.cilindrada})
        return attrs

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo=1):
        Vehiculo.__init__(self, color, ruedas)
        if tipo == 1:
            self.tipo='urbana'
        elif tipo == 2:
            self.tipo='deportiva'

    def mostrarAtributos(self):
        attrs = {}
        attrs.update(Vehiculo.mostrarAtributos(self))
        attrs.update({'tipo': self.tipo})
        return attrs

class Camioneta(Coche):
    def __init__(self, color, ruedas, vel, cil, carga):
        Coche.__init__(self, color, ruedas, vel, cil)
        self.carga = carga

    def mostrarAtributos(self):
        attrs = {}
        attrs.update(Coche.mostrarAtributos(self))
        attrs.update({'carga': self.carga})
        return attrs

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, vel, cil):
        Bicicleta.__init__(self, color, ruedas, tipo)
        self.velocidad = vel
        self.cilindrada = cil

    def mostrarAtributos(self):
        attrs = {}
        attrs.update(Bicicleta.mostrarAtributos(self))
        attrs.update({'velocidad': self.velocidad, 'cilindrada' : self.cilindrada})
        return attrs

class ListaVehiculos:
    __todos_los_vehiculos = []

    def agregarVehiculo(self, el):
        ListaVehiculos.__todos_los_vehiculos.append(el)

    def catalogarVehiculo(self, ruedas=0):
        cant = 0
        for el in ListaVehiculos.__todos_los_vehiculos:
            if(el.ruedas == ruedas):
                print(type(el).__name__)
                print(type(el).mostrarAtributos(el))
                cant += 1
        print(f'se han encontrado {cant} vehiculos con {ruedas} ruedas')
    

mi_coche = Coche('rojo', 4, 150, 1000)
mi_bici = Bicicleta('verde', 2, 2)
mi_camio = Camioneta('azul', 4, 130, 1600, 420)
mi_moto = Motocicleta('negro', 2, 1, 160, 1300)

misVehiculos = ListaVehiculos()
misVehiculos.agregarVehiculo(mi_bici)
misVehiculos.agregarVehiculo(mi_camio)
misVehiculos.agregarVehiculo(mi_coche)
misVehiculos.agregarVehiculo(mi_moto)

misVehiculos.catalogarVehiculo(4)