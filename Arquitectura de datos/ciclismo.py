def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("El dato que ingreso no es numerico, intentelo nuevamente.")

def read_num(mensaje):
    while True:
        try:
            numes = int(input(mensaje))
            if numes <= 0:
                raise ValueError
            return numes
        except ValueError:
            print("El valor tiene que ser mayor a 0. ")

def read_str(mensaje):
    while True:
        word = input(mensaje)
        if word.isnumeric():
            print("Tiene que ingresar una palabra.")
        elif word.isalpha():  
            return word
  
napl = [] #Lista de los nombres de los participantes
nate = [] #Lista de los nombres del equipo al que pertenece


#inicio de codigo.
lap = read_int("Ingrese el número de participantes que tiene su carrera: ")
for i in range(lap):
    name = read_str("Ingrese el nombre del ciclista: ")
    napl.append(name)
    name_team = read_str(f"Ingrese el nombre del equipo al que pertenece el ciclista {name}. ")
    nate.append(name_team)

print(napl)
print(nate)




# v1