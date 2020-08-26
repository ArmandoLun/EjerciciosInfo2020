class Vehiculo():
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas
class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		Vehiculo.__init__(self, color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada
	def __str__(self):
		return (f"Coche de color {self.color}, tiene {self.ruedas} ruedas, velocidad maxima de {self.velocidad} km/h y {self.cilindrada} cc")
