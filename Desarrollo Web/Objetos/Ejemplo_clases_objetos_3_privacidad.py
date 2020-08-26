class Alumno():
	""" Clase Alumno """
	# Atributos de clase: son atributos generales para todos los objetos instanciados.
	# __ doble guión bajo no indica a un atributo o método como privabado.
	__cantidad_alumnos = 0
	__total_notas      = 0
	
	# Constructor: éste método se ejecuta automáticamente al crear un objeto.
	def __init__(self, nom_alumno, nota_alumno):
		# Atributos de instancia: son atributos propios o particulares un un objeto.
		self.nombre	= nom_alumno
		self.nota =   nota_alumno
		# Alumno.__cantidad_alumnos += 1
		# Alumno.__total_notas += nota_alumno
		self.__set_cantidad_alumnos()
		self.__set_total_notas()

	def mostrar_nota(self):
		print('\nLa nota de ',self.nombre,' es: ',self.nota)

	def get_cantidad_alumnos(self):	
		return self.__cantidad_alumnos

	def __set_cantidad_alumnos(self):
		Alumno.__cantidad_alumnos +=1

	def __set_total_notas(self):
		Alumno.__total_notas += self.nota

	def get_promedio(self):
		promedio = self.__total_notas / self.__cantidad_alumnos
		return 	promedio

class ListaAlumno():
	__lista_alumnos = []
	def __init__(self,l_alumno):
		__lista_alumnos.append(l_alumno)

	def get_lista_alumnos(self):
		for a in self.__lista_alumnos:
			print(a)
			
nombre = "Juan"
nota   = 8
mi_alumno = Alumno(nombre,nota)

nombre = "Alejandra"
nota   = 9
mi_alumno2 = Alumno(nombre,nota)

nombre = "Alan"
nota   = 7
mi_alumno3 = Alumno(nombre,nota)

print()
mi_alumno.mostrar_nota()
mi_alumno2.mostrar_nota()
mi_alumno3.mostrar_nota()


print("Cantidad total de alumnos: ",mi_alumno.get_cantidad_alumnos())
print("El promedio general es: ",mi_alumno2.get_promedio())