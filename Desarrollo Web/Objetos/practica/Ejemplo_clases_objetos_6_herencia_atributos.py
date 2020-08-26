class PersonajeBase():

	def __init__(self,nombre,agilidad,resistencia,poder_ataque,clase,salud = 100):
		self.nombre 	  = nombre
		self.agilidad 	  = agilidad
		self.resistencia  = resistencia
		self.poder_ataque = poder_ataque
		self.salud 	      = salud
		self.clase        = clase

	def saltar(self):
		pass

	def avanzar(self):
		pass

	def retroceder(self):
		pass

	def agachar(self):
		pass

	def atacar(self):
		pass

	def defender(self):
		pass

	def __str__(self):	
		return "Nombre: {}\nClase: {}\nAgilidad: {}\nResistencia:  {}\nPoder: {}\n".format(self.nombre,self.clase,self.agilidad,self.resistencia,self.poder_ataque)



class Piedra(PersonajeBase):

	def __init__(self,nombre="STONE WARRIOR",agilidad=50,resistencia=90,poder_ataque=75,arma="GARROTE DE PIEDRA",clase="PIEDRA"):
		super().__init__(nombre,agilidad,resistencia,poder_ataque,clase)
		self.arma = arma

	def __str__(self):
		return super().__str__()+"Arma: {}\n".format(self.arma)

class Fuego(PersonajeBase):

	def __init__(self,nombre="PRINCESA FLAMA",agilidad=80,resistencia=70,poder_ataque=80,clase="FUEGO"):
		super().__init__(nombre,agilidad,resistencia,poder_ataque,clase)



personaje_1 = Piedra()
personaje_2 = Fuego()

print(personaje_1)
print(personaje_2)




