import csv
from clase7 import ViajeroFrecuente

def _menu(numero,lista):
	print(f"[Numero de viajero]: {numero} \n ---Menu de opciones--- \n \n [Consultar] -> c \n [Acumular] -> a \n [Canjear] -> n \n [Fin] -> f")
	var = input("Ingrese opcion: ")
	i = int(numero) - 1
	while (var != "f"):
		if lista[i].getnum() == numero:
			if var == "c":
				print(f"\n La cantidad de millas del viajero {numero} es de: [{lista[i].getmillas()}]")
				
			elif var == "a":
				x = int(input("\n Ingrese cantidad de millas a acumular: "))
				b = lista[i].acumularMillas(x)
				print(f"\n Las millas acumuladas del viajero numero: {numero} ahora es de: {b}")
			elif var == "n":
				canj = int(input("\n Ingrese la cantidad de millas a canjear: "))
				lista[i].canjearMillas(canj)
			else:
				print("\n Ingreso mal la opcion.")
		else:
			i = i + 1
		print(f"[Numero de viajero]: {numero} \n ---Menu de opciones--- \n \n [Consultar] -> c \n [Acumular] -> a \n [Canjear] -> n \n [Fin] -> f")
		var = input("Ingrese opcion: ")
		
if __name__ == "__main__":
	lista = []
	archivo = open("viajeros.csv")
	datos = csv.reader(archivo,delimiter = ",")

	for fila in datos:
		unviajero = ViajeroFrecuente(fila[0],fila[1],fila[2],fila[3])
		lista.append(unviajero)
	numviaj = input("Ingrese un numero de un viajero frecuente: ")
	_menu(numviaj,lista)
	i = 0
	while i < len(lista)-1:
		if lista[i] > lista[i+1]:
			print(f"\nEl viajero: {lista[i].getnombre()} posee mas millas acumuladas que el viajero: {lista[i+1].getnombre()}")
		else:
			print(f"\nEl viajero: {lista[i+1].getnombre()} posee mas millas acumuladas que el viajero: {lista[i].getnombre()}")
		aux = input(f"\nDesea acumular millas para el viajero {lista[i].getnombre()}? si o no: ")
		if aux == "si":
			cant = int(input("Ingrese la cantidad de millas que desea acumular: "))
			lista[i] = cant + lista[i]
			print(f"\nAhora su cantidad de millas es de: {lista[i].getmillas()}")
		aux2 = input(f"Desea canjear millas del viajero {lista[i].getnombre()} si o no: ")
		if aux2 == "si":
			cant = int(input("Ingrese la cantidad de millas que desea canjear: "))
			lista[i] = cant - lista[i]
			print(f"\nAhora su cantidad de millas es de: {lista[i].getmillas()}")
		aux3 = input(f"Desea comparar las millas del viajero {lista[i].getnombre()}  si o no: ")
		if aux3 == "si":
			v = int(input("Ingrese un valor para comparar: "))
			d = v == lista[i] 
			if d == True:
				print("Las millas son iguales al valor ingresado.")
			else: 
				print("Las millas son distintas al valor ingresado.")
		i=i+1
	print("\n")
	print("\n")
	print (f"[Numero pasajero]: {lista[i].getnum()} [DNI del viajero]: {lista[i].getdni()} [Nombre del viajero]: {lista[i].getnombre()} [Millas acumuladas del viajero]: {lista[i].getmillas()}")
