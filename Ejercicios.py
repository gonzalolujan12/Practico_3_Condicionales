#Ejercicio 1
edad = int(input("Por favor, ingresa tu edad: "))
if edad >= 18:
    print("Eres mayor de 18 años.")
else:
    print("Eres menor de 18 años.")


#Ejercicio 2
nota = int(input("Ingresar la nota:"))
if nota >=6:
    print("Esta Aprobado")
else:
    print("Esta Desaprobado")

#Ejercicio 3
numero= int(input("Ingresar un numero:"))
if numero % 2==0:
    print("Has ingresado un numero par")
else:
    print("Por favor ingresar un numero par")

#Ejercicio 4
edad = int(input("Ingresa la edad:"))
if edad <12:
    print("Es un Niño/a")
elif edad >=12 and edad <18:
    print("Es Adolescente")
elif edad >=18 and edad <30:
    print("Es Adulto/a Joven")
elif edad >=30:
    print("Es Adulto/a")


#Ejercicio 5
usuario= input("Introducir una contraseña:")
if len(usuario) >14:
    print ("El nombre del usuario es muy largo, deberia ser de 14 caracteres como maximo")
elif len(usuario) <8:
    print ("El nombre del usuario es muy corto, deberia ser de 8 caracteres como minimo")
else:
    print("El nombre del usuario es válido")

#Ejercicio 6
from statistics import mode,median, mean
import random
numeros_aleatorios= [random.randint (1,100)for i in range (50)]
print(numeros_aleatorios)

print(mean(numeros_aleatorios))
print(median(numeros_aleatorios))
print(mode(numeros_aleatorios))

if mean(numeros_aleatorios ) > median(numeros_aleatorios) and median(numeros_aleatorios)> mode(numeros_aleatorios):
   print("Sesgo positivo o la derecha")
elif mean(numeros_aleatorios ) < median(numeros_aleatorios) and median(numeros_aleatorios)< mode(numeros_aleatorios):
   print("Sesgo negativo o la izquierda")
elif mean (numeros_aleatorios ) == median(numeros_aleatorios) == mode(numeros_aleatorios):
   print ("Sin sesgo")

#Ejercicio 7
nombre = input("Ingresa una palabra: ")
if nombre.startswith(("a","e", "i","o","u")):
    print("La palabra comienza con vocal")
else:
    print("La palabra  NO comienza  en vocal")

if nombre.endswith(("a","e","i","o","u")):
    print("La palabra termina en vocal")
else:
    print("La palabra Termina NO vocal")

#Ejercicio 8
entrada = input("Ingresa una palabra: ")
def mostrar_menu():
    print("Selecciona una opción:")
    print("1. Convertir a Minuscula")
    print("2. Convertir a Titulo")
    print("3. Convertir a Mayuscula")
mostrar_menu()
opcion = input("Ingrese el número de la opción deseada: ")

if opcion =="1":
    print(entrada.lower())
elif opcion =="2":
    print (entrada.title())
elif opcion == "3":
    print(entrada.upper())

#Ejercicio 9

entrada = input("La magnitud  del terrremoto es : ")
if entrada < "3":
    print("Muy Leve", "(Imperceptible)")
elif entrada == "3" and entrada < "4":
    print ("Leve", "(Ligeramente perceptible)")
elif entrada == "4" and entrada < "5":
    print("Moderado", "(Sentido por personas, pero generalmente no causa daño)")
elif entrada == "5" and entrada < "6":
    print("Fuerte", "(Puede causar daños en estructuras débiles")
elif entrada == "6" and entrada < "7":
    print("Muy fuerte", "(Puede causar daños significativos")
elif entrada >= "7":
    print("Extremo", "(Puede causar graves daños a gran escala)")  

#Ejercicio 10


hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").upper()
mes = int(input("Ingrese en que mes se encuentra (1 al 12): "))
dia = int(input("Ingrese en que dia se encuentra (1 al 31): "))

if (hemisferio == "N" and ((mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<=20))) or (hemisferio == "S" and ((mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es invierno")
elif (hemisferio == "N" and ((mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<=20))) or (hemisferio == "S" and ((mes==9 and dia>=21) or (mes==10) or (mes==11) or (mes==12 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es primavera")
elif (hemisferio == "N" and ((mes==6 and dia>=21) or (mes==7) or (mes==8) or (mes==9 and dia<=20))) or (hemisferio == "S" and ((mes==12 and dia>=21) or (mes==1) or (mes==2) or (mes==3 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es verano")
elif (hemisferio == "N" and ((mes==9 and dia>=21) or (mes==10) or (mes==11) or (mes==12 and dia<=20))) or (hemisferio == "S" and ((mes==3 and dia>=21) or (mes==4) or (mes==5) or (mes==6 and dia<=20))):
    print(f"Hoy es {dia}/{mes} en el hemisferio {hemisferio}, es otoño")