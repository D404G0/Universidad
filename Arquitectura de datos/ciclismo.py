numes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

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
        try:
            word = input(mensaje)
            for k in len(range(word)):
                if k in word == numes:
                    raise ValueError
                return word
        except ValueError:
            print("Tiene que ingresar una palabra.")

napl = []  #Lista de los nombres de los participantes


#inicio de codigo.
lap = read_int("Ingrese el número de participantes que tiene su carrera: ")
for i in range(lap):
    name_participant = napl.append(read_str("Ingrese el nombre del ciclista: "))




# v1