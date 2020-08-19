class Producto:
    def __init__(self, nom, cant):
        self.nombre = nom
        self.cantidad = cant

    def calcular(self, ens):
        cantEns = self.cantidad / len(ens)
        restoEns = self.cantidad % len(ens)
        for en in ens:
            print(f'{en} recibira {cantEns} unidades de {self.nombre}')
        print(f'se guardaran {restoEns} unidades de {self.nombre} para la proxima donacion')

class Perecedero(Producto):
    def __init__(self, nom, cant, diasCad):
        super().__init__(nom, cant)
        self.diasACaducar = diasCad

    def calcular(self, ens):
        super().calcular(ens)
        if self.diasACaducar < 10:
            print('La entrega debe hacerse en el dia actual')
        elif self.diasACaducar <=30:
            print('La entrega debe hacerse en una semana')
        else:
            print('queda libre la elección de la fecha de entrega siempre que no supere el mes')

class NoPerecedero(Producto):
    def __init__(self, nom, cant, tipo):
        super().__init__(nom,cant)
        self.tipo = tipo

    def calcular(self, ens):
        super().calcular(ens)
        print('queda libre la elección de la fecha de entrega siempre que no supere el mes')
    
leche = Perecedero('leche', 45, 15)
leche.calcular(['el chino de la esquina', 'mi vecina', 'facebook', 'nisuta'])