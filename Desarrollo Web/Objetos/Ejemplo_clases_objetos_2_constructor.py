class Alumno():
	""" Clase Alumno """
	# Atributos de clase: son atributos generales para todos los objetos instanciados.
	cantidad_alumnos = 0

	# Constructor: éste método se ejecuta automáticamente al crear un objeto.
	def __init__(self, nom_alumno, nota_alumno):
		# Atributos de instancia: son atributos propios o particulares un un objeto.
		self.nombre	= nom_alumno
		self.nota =   nota_alumno
		Alumno.cantidad_alumnos += 1

	def mostrar_nota(self):
		print('\nLa nota de ',self.nombre,' es: ',self.nota)


nombre = "Juan"
nota   = 8
mi_alumno = Alumno(nombre,nota)

nombre = "Alejandra"
nota   = 9
mi_alumno2 = Alumno(nombre,nota)

# print(mi_alumno.nombre)
# print(mi_alumno.nota)
mi_alumno.mostrar_nota()
mi_alumno2.mostrar_nota()

print(mi_alumno.cantidad_alumnos)
print(mi_alumno2.cantidad_alumnos)
