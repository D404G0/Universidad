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
        
#Funcion para gener un numero aleatorio de 0 a 60.
def second_minutes():
    random.randrange(0, 59)

#Funcion paara generar un nuemro aleatorio desde 80 hasta 100
def hour():
    random.randrange(80, 100)
  
napl = [] #Lista de los nombres de los participantes
nate = [] #Lista de los nombres del equipo al que pertenece
time = [] #Lista para guardar el tiempo del jugador


#inicio de codigo.
part = read_int("Ingrese el número de participantes que tiene su carrera: ")
for i in range(part):
    name = read_str("Ingrese el nombre del ciclista: ")
    napl.append(name)
    name_team = read_str(f"Ingrese el nombre del equipo al que pertenece el ciclista {name}. ")
    nate.append(name_team)
    time_var = (f"Hora{hour()} - Minutos{second_minutes} - Segundos{second_minutes}.")
    time.append(time_var)


print(napl)
print(nate)
print(time)




# v2
