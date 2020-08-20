import datetime
import operator
class Pizza:
    tipos = [
        {'nombre': 'A molde', 'precio': 0.3},
        {'nombre': 'A la parrilla', 'precio': 0.4},
        {'nombre': 'A la piedra', 'precio': 0.5}
    ]
    tamanios = [
        {'nombre': '8 porciones','precio': 0.2},
        {'nombre': '10 porciones','precio': 0.25},
        {'nombre': '12 porciones','precio': 0.3}
    ]

    variedades = [
        {'nombre': 'Napolitana', 'precio': 10,
        'ingredientes': ['Tomate', 'Queso', 'Huevo']},
        {'nombre': 'Calabresa', 'precio': 12,
        'ingredientes': ['Tomate', 'Queso', 'Salamin']},
        {'nombre': 'Fugazzeta', 'precio': 9,
        'ingredientes': ['Queso',]},
        {'nombre': '4 Quesos', 'precio': 14,
        'ingredientes': ['Queso']},
        {'nombre': 'Comun', 'precio': 10,
        'ingredientes': ['Tomate', 'Queso']},
        {'nombre': 'Especial', 'precio': 12,
        'ingredientes': ['Tomate', 'Queso', 'Jamon']}
    ]

    def __init__(self, idPizza, idTipo, idTamanio):
        self.nombre = Pizza.variedades[idPizza]['nombre']
        self.tipo = Pizza.tipos[idTipo]
        self.tamanio = Pizza.tamanios[idTamanio]
        self.precio = Pizza.variedades[idPizza]['precio'] + (Pizza.variedades[idPizza]['precio'] * Pizza.tipos[idTipo]['precio']) + (Pizza.variedades[idPizza]['precio'] * Pizza.tamanios[idTamanio]['precio'])
    
    def __repr__(self):
        return f"Pizza {self.nombre} {self.tamanio['nombre']} {self.tipo['nombre']}"

class Pedido:
    idPedido = 0

    def __init__(self, nombreCli):
        Pedido.idPedido +=1
        self.id = Pedido.idPedido
        self.nombreCliente = nombreCli
        self.pizzasPedido = []
        self.fecha = datetime.datetime.now().date()
        self.demora = 0
        self.horaEstimada = 0
    
    def __repr__(self):
        return f"Pedido nº {self.id}: a nombre de {self.nombreCliente}. Ha pedido: {self.pizzasPedido}. Hora estimada: {self.horaEstimada}"

    def agregarPizza(self, pizza):
        self.pizzasPedido.append(pizza)
        self.demora += 15
        self.horaEstimada = str((datetime.datetime.now() + datetime.timedelta(minutes=self.demora)).time())

class ListaPedidos:
    todosLosPedidos = []

    def __repr__(self):
        return f"Pedidos realizados: {ListaPedidos.todosLosPedidos}"

    def agregarPedido(self, pedido):
        ListaPedidos.todosLosPedidos.append(pedido)

    def variedadMasPedida(self):
        lis = self.todosLosPedidos
        pedidos = list()
        for el in lis: pedidos.extend(el.pizzasPedido)
        pedidos.sort(key=operator.attrgetter("nombre"))
        return max(set(pedidos), key = operator.attrgetter("nombre")).nombre

    def tipoMasPedido(self):
        lis = self.todosLosPedidos
        pedidos = list()
        for el in lis: pedidos.extend(el.pizzasPedido)
        pedidos.sort(key = lambda x : x.tipo['nombre'])
        return max(set(pedidos), key = operator.attrgetter("tipo")).tipo['nombre']

    def ingresosPorPeriodo(self):
        inicio = input('ingrese inicio (anio/mes/dia): ')+'/'
        fin = input('ingrese fin (anio/mes/dia): ')+'/'
        inicioP = []
        finP = []
        actual = ''
        for c in inicio:
            if c != '/':
                actual += c
            else:
                inicioP.append(int(actual))
                actual=''

        for c in fin:
            if c != '/':
                actual += c
            else:
                finP.append(int(actual))
                actual=''
        inicioP = datetime.date(inicioP[0],inicioP[1],inicioP[2])
        finP = datetime.date(finP[0],finP[1],finP[2])
        recaudacion=0
        for i in ListaPedidos.todosLosPedidos:
            if(i.fecha > inicioP and i.fecha < finP):
                for p in i.pizzasPedido:
                    print(f'pizza {p.nombre} {p.tamanio} {p.tipo}')
                    recaudacion += p.precio
        print(f'Recaudacion entre {inicioP} y {finP}: {recaudacion}')
        """for i in ListaPedidos.todosLosPedidos:
            if datetime.date(anio,mes,dia) > i.fecha:
                print(i)"""
class Menu:

    def mostrarTamanios(self):
        for i in range(0, len(Pizza.tamanios)):
            print('{}: {}'.format(i, Pizza.tamanios[i]['nombre']))

    def mostrarTipos(self):
        for i in range(0, len(Pizza.tipos)):
            print('{}: {}'.format(i, Pizza.tipos[i]['nombre']))

    def mostrarVariedades(self):
        variedades = Pizza.variedades
        for i in range(0, len(variedades)):
            print('{}: {}'.format(i, variedades[i]['nombre']))
            for ing in variedades[i]['ingredientes']:
                print(ing, end=" - ")
            print()

    def calcularPrecio(self, precio, tipo, tamanio):
        pfinal = precio + (precio*Pizza.tipos[tipo]['precio']) + (precio*Pizza.tamanios[tamanio]['precio'])
        print('Precio final:', pfinal)
    
    def tomarPedido(self, nombreCli=None):
        print("---- variedades ----")
        self.mostrarVariedades()
        idPizza = int(input('Escoja su pizza: '))
        print("---- tamanios ----")
        self.mostrarTamanios()
        tamanio = int(input('Tamanio de su pizza? : '))
        print("---- cocciones ----")
        self.mostrarTipos()
        tipo = int(input('Tipo de coccion? : '))
        self.calcularPrecio(Pizza.variedades[idPizza]['precio'], tipo, tamanio)
        if nombreCli == None:
            nombre = input('Ingrese su nombre: ')
            globals()[f"{nombre}{Pedido.idPedido}"] = Pedido(nombre)
        else:
            nombre = nombreCli
        globals()[f"{nombre}{Pedido.idPedido}"].agregarPizza(Pizza(idPizza,tipo,tamanio))
        res = input('Desea algo mas? (s / n): ')
        
        if res == 's':
            return self.tomarPedido(nombre)
        else:
            print('Ud ha realizado el pedido:')
            print(globals()[f"{nombre}{Pedido.idPedido}"])
            lp.agregarPedido(globals()[f"{nombre}{Pedido.idPedido}"])
    
m = Menu()
lp = ListaPedidos()
m.tomarPedido()
#m.tomarPedido()
#print("Pizza mas pedida: ", lp.variedadMasPedida())
#print("Tipo mas pedido: ", lp.tipoMasPedido())
lp.ingresosPorPeriodo()