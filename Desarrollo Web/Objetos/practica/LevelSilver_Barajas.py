from random import shuffle
class Carta:
	def __init__(self, figura, valor):
		self.figura = figura
		self.valor = valor

	def __repr__(self):
		return "{} de {}".format(self.valor,self.figura)


class Baraja:
	def __init__(self):
		figuras = ['Copas', 'Bastos', 'Oro', 'Espadas']
		valores = ["1","2","3","4","5","6","7","10","11","12"]
		self.descarte = []
		self.cartas =[Carta(figura,valor) for figura in figuras for valor in valores]

	def barajar(self):
		return shuffle(self.cartas)

	def siguienteCarta(self):
		if (len(self.cartas)== 0):
			raise ValueError("Se han repartido todas las cartas")
		cartaRepartida = self.cartas.pop()
		self.descarte.append(cartaRepartida)
		print(cartaRepartida) 

	def cartasDisponibles(self):
		return len(self.cartas)

	def darCartas(self, cantidad):
		if (self.cartasDisponibles() < cantidad):
			raise ValueError("No disponemos de suficientes cartas")
		print("estas son sus ",cantidad," de cartas: ")
		for _ in range(cantidad):
			cartaRepartida = self.siguienteCarta()
			

	def cartasMonton(self):
		if(len(self.descarte) == 0):
			print("Todavia no se partió ninguna carta")
		print(self.descarte)
		

	def mostrarBaraja(self):
		print(self.cartas)

mazo = Baraja()
mazo.mostrarBaraja()
mazo.barajar()
mazo.mostrarBaraja()
mazo.siguienteCarta()
mazo.mostrarBaraja()
print("cartas disponibles ",mazo.cartasDisponibles())
mazo.siguienteCarta()
print("cartas disponibles ",mazo.cartasDisponibles())
print("Descarte:")
mazo.cartasMonton()
mazo.darCartas(6)
print("Descarte:")
mazo.cartasMonton()
