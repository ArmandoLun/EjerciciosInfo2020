#Clase agenda#
class Agenda:
	listaContactos = []
	#Metodo para añadir contactos al atributo de clase "listaContactos"#
	def AnadirContacto(self):
		print("-----------Añadir Contacto------------------")
		nombre = input("Ingrese nombre del contacto:")
		telefono = int(input("Ingrese el numero de telefono del contacto:"))
		email = input("ingrese el email del contacto:")
		contacto = Contacto(nombre,telefono,email)
		Agenda.listaContactos.append(contacto)
		print("Cargando...")
		print("El contacto se añadio correctamente")
		print("Regresando al menu...")
		self.menu()
	#Muestra los contactos que estan dentro del atributo de clase "listaContactos"#
	def ListaDeContactos(self):
		cont = 1;
		print("--------------Lista de Contactos---------")
		for contacto in self.listaContactos:
			print("\nContacto Nº",cont,":",contacto,"\n")
			cont+=1
		print("Regresando al menu...")
		self.menu()
	#Metodo que Busca un contacto POR NOMBRE#
	def BusquedaContacto(self):
		resultados = list()
		print("----------Busqueda de Contacto---------")
		nombre = input("Ingrese el nombre del contacto buscado:").lower()
		print("Cargando...")
		try:
			for contacto in self.listaContactos:
				nombreC = contacto.nombre.lower()
				if(nombreC==nombre):
					resultados.append(contacto)
			cont = 1;
			print("---------Lista de Contactos Encontrados--------")
			for contacto in resultados:
				print("\nContacto Nº",cont,":",contacto,"\n")
				cont+=1
		except:
			print("no se encontro ningun contacto con ese nombre")
		finally:
			print("Regresando al menu...")
			self.menu()
	#Metodo para editar un contacto de la lista#
	def EditarContacto(self):
		print("----------Edicion De Contacto---------")
		bandera = True
		opcion = 0
		encontrado = False
		while(bandera):
			try:
				encontrado=False
				telEditado = int(input("Ingrese el numero celular del contacto:"))
				for contacto in self.listaContactos:
					if(telEditado == contacto.telefono):
						indiceEditar = self.listaContactos.index(contacto)
						print("Se encontro un contacto:")
						print(self.listaContactos[indiceEditar])
						encontrado = True
				if(not encontrado):
					raise
				opcion = 0
				while(opcion != 1 and opcion != 2 and opcion != 3 and encontrado):
					try:
						opcion = int(input("Que desea editar?\n1.Nombre\n2.Telefono\n3.Email\nIngrese un numero:"))
						if(opcion == 1):
							nombreNuevo = input("ingrese nuevo nombre del contacto")
							self.listaContactos[indiceEditar].setNombre(nombreNuevo)
							print("Cargando...\nNombre Actualizado!")
							raise
						if(opcion == 2):
							telefonoNuevo = input("ingrese nuevo numero del contacto")
							self.listaContactos[indiceEditar].setTelefono(telefonoNuevo)
							print("Cargando...\nNumero Actualizado!")
							raise
						if(opcion == 3):
							emailNuevo = input("ingrese nuevo email del contacto")
							self.listaContactos[indiceEditar].setEmail(emailNuevo)
							print("Cargando...\nEmail Actualizado!")
							raise
					except ValueError:
						print("Por favor ingrese un numero")
					except:
						opcion = 0
						while(opcion != 1 and opcion != 2):
							opcion = int(input("Desea continuar?\n1.Si\n2.No\nIngrese Numero:"))
							if(opcion == 1):
								continue
							elif(opcion == 2):
								bandera = False
			except ValueError:
				print("Ingrese solo numeros")
				opcion = 0
				while(opcion != 1 and opcion != 2):
					opcion = int(input("Desea continuar?\n1.Si\n2.No\nIngrese Numero:"))
					if(opcion == 1):
						continue
					elif(opcion == 2):
						bandera = False
			except:
				print("No se encontro un contacto con ese numero")
				opcion = 0
				while(opcion != 1 and opcion != 2):
					opcion = int(input("Desea continuar?\n1.Si\n2.No\nIngrese Numero:"))
					if(opcion == 1):
						continue
					elif(opcion == 2):
						bandera = False
			finally:
				if(not bandera):
					print("Regresando al menu...")
					self.menu()
	#El metodo menu que conecta todos los metodos#
	def menu(self):
		print("-----------------MENU------------------")
		opcion = int(input("1.Añadir Contacto\n2.Lista de Contactos\n3.Buscar Conctacto\n4.Editar contacto\n5.Cerrar Agenda\nIngrese un numero:"))
		if(opcion == 1):
			self.AnadirContacto()
		if(opcion == 2):
			self.ListaDeContactos()
		if(opcion == 3):
			self.BusquedaContacto()
		if(opcion == 4):
			self.EditarContacto()
		elif(opcion == 5):
			return 0

#Clase Contacto para crear contactos y añadirlos a la agenda#
class Contacto:
	def __init__(self,nombre,telefono,email):
		self.nombre = nombre
		self.telefono = telefono
		self.email = email

	def setNombre(self,nombre):
		self.nombre = nombre

	def setTelefono(self,telefono):
		self.telefono = int(telefono)

	def setEmail(self,email):
		self.email = email	

	def __str__(self):
		return (f"\nNombre Contacto:{self.nombre}\nTelefono:{self.telefono}\nEmail:{self.email}")

#####   MAIN  #######
agenda = Agenda()
agenda.menu()