#Definiendo Clases y metodos.
#############################################################
#Super clase lista

#Superclase vehiculo
class Vehiculo():
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas
	def __str__(self):
		return (f"coche de color {self.color} con {self.ruedas} ruedas")

#SubClase coche, añade velocidad y cilindrada
class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		Vehiculo.__init__(self, color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada
	#print para la instancia
	def __str__(self):
		return (f"Coche de color {self.color}, tiene {self.ruedas} ruedas, velocidad maxima de {self.velocidad} km/h y {self.cilindrada} cilindrada")

#subsubclase camioneta, añade carga.
class Camioneta(Coche):
	def __init__(self, color, ruedas, velocidad, cilindrada, carga):
		Coche.__init__(self, color, ruedas, velocidad, cilindrada)
		self.carga = carga
	#print para la instacia 
	def __str__(self):
		return (f"Coche de color {self.color}, tiene {self.ruedas} ruedas, velocidad maxima de {self.velocidad} km/h y {self.cilindrada} cilindrada y carga {self.carga} kg")

#subsubclase bicicleta, Tipo: urbana o deportiva. True es urbana. False es deportiva
class Bicicleta(Vehiculo):
	def __init__(self,color,ruedas,tipo):
		Vehiculo.__init__(self,color,ruedas)
		if (tipo == True):
			self.tipo = "urbana"
		else:
			self.tipo = "deportiva"

class Motocicleta(Bicicleta):
	def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
		Bicicleta.__init__(self,color,ruedas,tipo)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

class listaVehiculos:
	def __init__(self):
		self.listaVehiculos = list()

	def setListaV(self,vehiculo):
		self.listaVehiculos.append(vehiculo)

	def catalogoBasico(self):
		cont = 1
		for objeto in self.listaVehiculos:
			print("elemento ",cont,": ",objeto,"DEL TIPO:",type(objeto).__name__)
			cont+= 1

	def catalogoModif(self, ruedas = 0):
		cont = 1
		cant = 0
		for objeto in self.listaVehiculos:
			if (objeto.ruedas == ruedas):
				print("elemento ",cont,": ",objeto,"DEL TIPO:",type(objeto).__name__)
				cant += 1
			cont+= 1
		print(f"se han encontrado {cant} vehiculo con {ruedas} ruedas")


#############################################################
#"MAIN de mi programa"
#############################################################
lista = listaVehiculos()
cocheson = Coche("verde",4,200,3.0)
camionetota = Camioneta("Roja",4,250,5.0,300)
motaza = Motocicleta("Blanca",2,True,100,2.0)
lacleta = Bicicleta("Morada",2,False)
lista.setListaV(cocheson)
lista.setListaV(camionetota)
lista.setListaV(motaza)
lista.setListaV(lacleta)
lista.catalogoBasico()
lista.catalogoModif(4)