import readchar

#Parte 1
nombre = input ("Ingresa tu Nombre: ")
print ("Bienvenido,", nombre)

#Parte 2, se utiliza la tecla w como "up" debido a que no lee correctamente la flecha arriba del teclado

while True:
    teclas = readchar.readkey()
    print ("Tecla Leida:", teclas)
    if teclas == 'w' or teclas == 'W':
        break