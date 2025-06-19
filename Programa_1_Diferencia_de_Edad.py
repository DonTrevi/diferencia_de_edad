#Este programa sirve para saber quien es mayor de dospersonas y por cuanto
#Aquí tomamos los datos del usuario:
#Nombre y edad de la primera persona:
print("Este programa sirve para calcular la diferencia de edad de dos personas")
print("El programa requiere el nombre de ambos y sus edades")
print("Escriba su nombre: ")
nom1 = input()
print("Escriba su edad: ")
edad1 = int(input())
#Nombre y edad de la segunda persona:
print ("Escriba el segundo nombre: ")
nom2 = input()
print ("Escriba la segunda edad: ")
edad2 = int(input())

#Estas comparaciones sirven para que no de un número negativo en la 
#resta de las edades y además muestra la diferencia de edad
if edad1 > edad2:
	diferencia = edad1 - edad2
	print("La diferencia de edad es de: ",diferencia)
	
if edad1 < edad2:
	diferencia = edad2 - edad1
	print("La diferencia de edad es de: ",diferencia)

#Aquí lanza el resultado final, quién es mayor
if edad1 > edad2:
	print(nom1 + " es mayor a " + nom2)
if edad1 < edad2:
	print(nom2 + " es mayor a " + nom1)

#Se agregó un nuevo comentario
