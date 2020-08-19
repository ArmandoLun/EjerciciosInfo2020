class Cuenta:
    def __init__(self, titular, cant=0):
        self.titular = titular
        self.cantidad = cant

    def mostrar(self):
        print(f'Titular: {self.titular}, Cantidad: {self.cantidad}')

    def ingresar(self, cant):
        if cant > 0:
            self.cantidad += cant
            print(f'Ingresados {cant}')
        else:
            print('Ingreso no realizado: cantidad invalida')
    
    def retirar(self, cant):
        self.cantidad -= cant
        print(f'Retirados {cant}')

c1 = Cuenta('Juan', 150)

c1.mostrar()
c1.ingresar(200)
c1.mostrar()
c1.ingresar(-100)
c1.retirar(600)
c1.mostrar()
