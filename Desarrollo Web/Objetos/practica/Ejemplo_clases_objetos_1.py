class Alumno():
	""" Clase Alumno """
	nombre = ""
	nota   = 0

	def mostrar_nota(self):
		print('\nLa nota de ',self.nombre,' es: ',self.nota)


mi_alumno = Alumno()
mi_alumno.nombre = "Juan"
mi_alumno.nota   = 8

mi_alumno2 = Alumno()
mi_alumno2.nombre = "Martina"
mi_alumno2.nota   = 5


mi_alumno.mostrar_nota()
mi_alumno2.mostrar_nota()
	

# print(mi_alumno2.__doc__)


# num = "12"
# print(type(num))
# print(num.__doc__)
# print(num.__dir__())

# print(type(mi_alumno))
# print(mi_alumno.__doc__)
# print(mi_alumno.__dir__())



