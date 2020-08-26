#Clases#########################
class triangulo():
	#Constructor por defeceto
	def __init__(self,lado1,lado2,lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	#metodo para determinar el tipo de triangulo
	def tipoTriangulo(self):
		if (self.lado1 != self.lado2 and self.lado2 != self.lado3 and self.lado1 != self.lado3):
			print("Triangulo Escaleno")
		elif ((self.lado1 == self.lado2 and self.lado1 != self.lado3) or (self.lado1 == self.lado3 and self.lado2 != self.lado1) or (self.lado2 == self.lado3 and self.lado2 != self.lado1)):
			print("Triangulo Isosceles")
		elif (self.lado1 == self.lado2 and self.lado2 == self.lado3):
			print("Triangulo Equilatero") 
	#metodo para determinar cual es el mayor lado del triangulo	
	def mayorLado(self):
		if (self.lado1 > self.lado2 and self.lado1>self.lado3):
			print("lado1 es el mayor lado, su tamaño es:",self.lado1)
		elif (self.lado2 > self.lado1 and self.lado2>self.lado3):
			print("lado2 es el mayor lado, su tamaño es:",self.lado2)
		elif (self.lado3 > self.lado2 and self.lado3>self.lado1):
			print("lado3 es el mayor lado, su tamaño es:",self.lado3)
		else:
			print("no hay un lado de mayor tamaño")

#Main###########################
triangulito = triangulo(2,1,3)
triangulito.tipoTriangulo()
triangulito.mayorLado()