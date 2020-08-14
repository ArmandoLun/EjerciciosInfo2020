def convertir_a_binario(num):
	resultado = bin(num)
	return resultado

def convertir_a_decimal(num):
	resultado = int(num,2)
	return resultado

def comprobar_binario(num):
	if (num[0] == '0' and num[1] == 'b'):
		bandera = False
		for i in range (2,len(num)):
			if (num[i] != '1' and num[i] != '0'):
				bandera = True
		if bandera:
			resultado = False
		else:
			resultado = True
	elif (num[0] == '-' and num[1] == '0' and num[2] == 'b'):
		bandera = False
		for i in range (3,len(num)):
			if (num[i] != '1' and num[i] != '0'):
				bandera = True
		if bandera:
			resultado = False
		else:
			resultado = True
	else:
		resultado = False
	return resultado

num = input ("ingrese un numero (binario o decimal):")

if str(num).isdecimal():
	resultado = convertir_a_binario(num)
elif comprobar_binario(num):
	resultado = convertir_a_decimal(num)
else:
	resultado = "nop"
print(resultado)