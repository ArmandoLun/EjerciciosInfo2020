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


	def __str__(self):
		return 'Nombre: '+self.nombre+'\nNota: '+str(self.nota)

	def __del__(self):
		print('eliminando objeto de memoria.')
			
class ListaAlumno():
	def __init__(self):	
		self.__lista_alumnos = list()

	def set_lista(self,alumno):
		self.__lista_alumnos.append(alumno)
	
	def get_lista(self):
		for a in self.__lista_alumnos:
			print(a)
	
	def __del__(self):
		print('eliminando objeto lista de memoria.')

lista = ListaAlumno()

nombre = "Juan"
nota   = 8
mi_alumno = Alumno(nombre,nota)

lista.set_lista(mi_alumno)

nombre = "Alejandra"
nota   = 9
mi_alumno2 = Alumno(nombre,nota)

lista.set_lista(mi_alumno2)

nombre = "Mariana"
nota   = 5
mi_alumno3 = Alumno(nombre,nota)

lista.set_lista(mi_alumno3)

lista.get_lista()

