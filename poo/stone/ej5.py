class Tiempo:
    def __init__(self, hora, mins=0, seg=0):
        self.__hora = hora
        self.__minutos = mins
        self.__segundos = seg

    def modificarHora(self, hora, mins, seg):
        self.__hora = hora
        self.__minutos = mins
        self.__segundos = seg

    def mostrarHora(self):
        print(f'hora: {self.__hora}, mins: {self.__minutos}, segundos: {self.__segundos}')

class prueba_hora(Tiempo):
    def __init__(self, hora, mins, seg):
        super().__init__(hora, mins, seg)
        super().mostrarHora()
        super().modificarHora(int(input('Ingrese hora: ')), int(input('Ingrese minutos: ')), int(input('Ingrese segundos: ')))
        super().mostrarHora()

prueba_hora(12,40,5)