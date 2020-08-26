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


class CamaraFoto(ArtefactoElectrico):
	def fotografiar(self):
		print("fotografiando..")



class ReproductorMp3(ArtefactoElectrico):
	def reproducir_musica(self):
		print("reproduciendo miusic..")
	def encender(self):
		print("encendiendo mp3..")

class Celular(ReproductorMp3,CamaraFoto,Telefono):
	pass

mi_celularcito = Celular()

mi_celularcito.encender()
mi_celularcito.apagar()
mi_celularcito.reproducir_musica()
mi_celularcito.fotografiar()

