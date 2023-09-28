import readchar, os


#Parte 1
nombre = input ("Ingresa tu Nombre: ")
print ("Bienvenido,", nombre)

#Parte 2, se utiliza la tecla w como "up" debido a que no lee correctamente la flecha arriba del teclado

while True:
    teclas = readchar.readkey()
    print ("Tecla Leida:", teclas)
    if teclas == 'w' or teclas == 'W':
        break

#Parte 3, cada vez que se oprime la tecla n se imprime un numero desde 0 y aumenta hasta 50

def terminal(numero): 
    os.system('cls' if os.name=='nt' else 'clear')
    print(numero)

n = 0

while n<=50:
    print("Ingrese Tecla")
    leer = readchar.readkey()
    if leer=='n' or leer=='N':
        terminal(n)
        n += 1