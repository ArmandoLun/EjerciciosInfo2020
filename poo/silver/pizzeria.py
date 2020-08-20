class Pizza:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __repr__(self):
        return f"Pizza {self.nombre} - Precio 8p: {self.precio}"

class Menu:
    __tipos = [
            {'nombre': 'A molde', 'precio': 0.3},
            {'nombre': 'A la parrilla', 'precio': 0.4},
            {'nombre': 'A la piedra', 'precio': 0.5}
        ]
    __tamanios = [
            {'nombre': '8 porciones','precio': 0.2},
            {'nombre': '10 porciones','precio': 0.25},
            {'nombre': '12 porciones','precio': 0.3}
        ]

    __variedades = [
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

    def mostrarTamanios(self):
        for i in range(0, len(Menu.__tamanios)):
            print('{}: {}'.format(i, Menu.__tamanios[i]['nombre']))

    def mostrarTipos(self):
        for i in range(0, len(Menu.__tipos)):
            print('{}: {}'.format(i, Menu.__tipos[i]['nombre']))

    def mostrarVariedades(self):
        for i in range(0, len(Menu.__variedades)):
            print('{}: {}'.format(i, Menu.__variedades[i]['nombre']))
            for ing in Menu.__variedades[i]['ingredientes']:
                print(ing, end=" - ")
            print()

    def calcularPrecio(self, precio, tipo, tamanio):
        pfinal = precio + (precio*tipo) + (precio*tamanio)
        print('Precio final:', pfinal)
    
    def tomarPedido(self):
        print("---- variedades ----")
        self.mostrarVariedades()
        idPizza = int(input('Escoja su pizza: '))
        print("Ud ha elegido: Pizza {}".format(Menu.__variedades[idPizza]['nombre']))
        print("---- tamanios ----")
        self.mostrarTamanios()
        tamanio = int(input('Tamanio de su pizza? : '))
        print("---- cocciones ----")
        self.mostrarTipos()
        tipo = int(input('Tipo de coccion? : '))
        self.calcularPrecio(Menu.__variedades[idPizza]['precio'], tipo, tamanio)
    
m = Menu()
m.tomarPedido()
