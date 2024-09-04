import random

#Funcion para ingresar valores numericos
def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("El dato que ingreso no es numerico, intentelo nuevamente.")

#Funcion para ingresar valores numericos con ecepciones
def read_num(mensaje):
    while True:
        try:
            numes = int(input(mensaje))
            if numes <= 0:
                raise ValueError
            return numes
        except ValueError:
            print("El valor tiene que ser mayor a 0. ")

#Funcion para ingresar palabras
def read_str(mensaje):
    while True:
        word = input(mensaje)
        if word.isnumeric():
            print("Tiene que ingresar una palabra.")
        elif word.isalpha():  
            return word
        
#Funcion para gener un numero aleatorio de 0 a 59.
def semi():
    k = random.randrange(0, 59)
    return k

#Funcion paara generar un nuemro aleatorio desde 80 hasta 100
def hour():
    x = random.randrange(80, 100)
    return x
  
#Diccionario donde se almacenara los datos del tour
tour_france = {"Nombre" : [], "Numero" : [], "Equipo" : [], "Tiempo" : [] }


#inicio de codigo.
part = read_int("Ingrese el número de participantes que tiene su carrera: ")
for i in range(part):
    name = read_str("Ingrese el nombre del ciclista: ")
    tour_france["Nombre"].append(name)

    id = read_num(f"Ingrese el numero del ciclista {name}: ")
    tour_france["Numero"].append(id)

    name_team = read_str(f"Ingrese el nombre del equipo al que pertenece el ciclista {name}: ")
    tour_france["Equipo"].append(name_team)

    print("------------------------------------------------")
    time_var = (f"{hour()}h - {semi()}' - {semi()}''.")
    tour_france["Tiempo"].append(time_var)

for participante in tour_france:
    for keys, values in participante:
        print(keys, "-", values)



# v4
