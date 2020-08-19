class Contacto:
    def __init__(self, nom, tel, email):
        self.nombre = nom
        self.telefono = tel
        self.email = email

    def __str__(self):
        cadena = "nombre: {} - telefono: {} - email: {}".format(self.nombre, self.telefono, self.email)
        return cadena

class Agenda:
    contactos = []

    def agregarContacto(self, nombre, tel, email):
        self.contactos.append(Contacto(nombre, tel, email))

    def mostrarContactos(self):
        for el in self.contactos:
            print(str(el))

    def buscarContacto(self, nom):
        for con in self.contactos:
            if con.nombre == nom:
                print(con)

    def editarContacto(self, nombre, edit, val): # edit: nombre del parametro a editar - val : nuevo valor
        for con in self.contactos:
            if con.nombre == nombre:
                setattr(con, edit, val)


def menu(p, a):
    if p == 1:
        print('Añadir contacto:')
        nom =input('Ingrese nombre')
        tel = int(input('Ingrese telefono'))
        email = input('Ingrese email')
        a.agregarContacto(nom, tel, email)
    elif p == 2:
        print('Mostrar contactos contacto:')
        a.mostrarContactos()
    elif p == 3:
        nom = input('Ingrese nombre:')
        a.buscarContacto(nom)
    elif p == 4:
        nom = input('Ingrese nombre')
        ed = input('Ingrese la propiedad a editar:')
        val = input('ingrese valor de la propiedad que desea editar')
        a.editarContacto(nom, ed, val)

a = Agenda()
p=0

while(p != 5):
    print('------Ingrese un numero:------')
    print('1: Añadir contacto')
    print('2: Mostrar contactos')
    print('3: Buscar contacto')
    print('4: Editar contacto')
    print('5: Salir')

    p =int(input('Ud elige:'))
    menu(p, a)