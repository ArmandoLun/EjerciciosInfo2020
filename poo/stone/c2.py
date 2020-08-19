class Bebida:
    def __init__(self, idBebida, cantLitros, precio, marca):
            self.id = idBebida
            self.cantLitros = cantLitros
            self.precio = precio
            self.marca = marca

    def __str__(self):
        return f'{type(self).__name__} id: {self.id}, marca {self.marca}, {self.cantLitros} litros, precio: {self.precio}'

class AguaMineral(Bebida):
    def __init__(self, idBebida, cantLitros, precio, marca, origen):
        super().__init__(idBebida, cantLitros, precio, marca)
        if origen == 1:
            self.origen = 'Manantial'
        elif origen == 2:
            self.origen = 'Ciudad'

class Gaseosa(Bebida):
    def __init__(self, idBebida, cantLitros, precio, marca, porcAzucar, promo):
        super().__init__(idBebida, cantLitros, precio, marca)
        self.porcionAzucar = porcAzucar
        self.precio -= 0.1*self.precio if promo == True else 0*self.precio

class Almacen:
    productos = []

    def cargarProductos(self, el):
        idRepetido = False
        for beb in Almacen.productos:
            if beb.id == el.id:
                idRepetido = True
            
        if not(idRepetido):
            Almacen.productos.append(el)
        else:
            print(f'Error, el id {el.id} ya esta registrado')

    def calcularTotal(self):
        total = 0
        for el in Almacen.productos:
            total += el.precio
        return total

    def calcularTotalMarca(self, marca):
        totalMarca = 0
        for el in Almacen.productos:
            if el.marca == marca:
                totalMarca += el.precio
        return totalMarca

    def eliminarProducto(self, id):
        for el in Almacen.productos:
            if el.id == id:
                Almacen.productos.pop(Almacen.productos.index(el))
                print(f'Elemento {el.id} eliminado')

    def mostrarProductos(self):
        for el in Almacen.productos:
            print(str(el))


b1 = AguaMineral(1, 2.5, 40, 'Sierra de los Padres', 1)
b2 = AguaMineral(2, 2.5, 40, 'Sierra de los Padres', 1)
b3 = AguaMineral(3, 2.5, 40, 'KIN', 1)
b4 = AguaMineral(2, 2.5, 40, 'Sierra de los Padres', 1)
b5 = AguaMineral(4, 2.5, 40, 'Sierra de los Padres', 1)
b6 = AguaMineral(5, 2.5, 40, 'Sierra de los Padres', 1)
al = Almacen()
al.cargarProductos(b1)
al.cargarProductos(b2)
al.cargarProductos(b3)
al.cargarProductos(b4)
al.cargarProductos(b5)
al.cargarProductos(b6)
print('precio total de los prods:',al.calcularTotal())
print('Precio total de marca Sierra de los Padres',al.calcularTotalMarca('Sierra de los Padres'))

al.eliminarProducto(4)
al.mostrarProductos()