class ArtefactoElectrico():
	def enceder(self):
		print("encendido...")

	def apagar(self):
		print("apagado...")

class Telefono(ArtefactoElectrico):
	def llamar (self):
		print ("llamando...")

	def colgar (self):
		print ("finalizando la llamada...")

	def encender(self):
		print("Cargando listas contactos")
		print("finalizando la carga")
		print("encendido")

class CamaraFoto(ArtefactoElectrico):
	def fotografia(self):
		print("fotografiando...")

class reproductorMp3(ArtefactoElectrico):
	def reproducir(self):
		print("reproducir musiquita...")

	def encender(self):
		print("Cargando listas favoritas")
		print("finalizando la carga")
		print("encendido")

class SmartPhone(Telefono,reproductorMp3,CamaraFoto):
	pass
