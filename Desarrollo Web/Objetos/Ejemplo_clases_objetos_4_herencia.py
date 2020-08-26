class ArtefactoElectrico():

	def encender(self):
		print("encendiendo..")

	def apagar(self):
		print("apagando..")


class Telefono(ArtefactoElectrico):

	def encender(self):
		print("encendiendo teléfono..")

	def llamar(self):
		print("llamando..")

	def colgar(self):
		print("fin de la llamada..")


arte_electico = ArtefactoElectrico()

telefonito = Telefono()
print("ArtefactoElectrico")
arte_electico.encender()
arte_electico.apagar()

print()
print("Telefono")
telefonito.encender()
telefonito.llamar()
telefonito.colgar()
telefonito.apagar()




