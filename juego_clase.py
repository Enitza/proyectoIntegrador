from clase import Juego
import readchar, os, random
archivos = os.listdir(r'C:\Users\enitz\Documents\CIENCIA DE DATOS\proyectoIntegrador\mapas')
seleccion = random.choice(archivos)
lectura = r'C:\Users\enitz\Documents\CIENCIA DE DATOS\proyectoIntegrador\mapas\\'+seleccion

archivo = Juego.leer_archivo(lectura)
posicion_inicial = (int(archivo[0]), int(archivo[1]))
posicion_final = (int(archivo[3]), int(archivo[2]))
laberinto = archivo[4:len(archivo)+1]
laberinto = "\n".join(["".join(fila) for fila in laberinto])


jugar = Juego(laberinto, posicion_inicial, posicion_final)

def main_loop(juego):
    px = juego.posicion_inicial[0]
    py = juego.posicion_inicial[1]
    mat = juego.conv_matriz(juego.laberinto)
    mat[px][py] = 'P'
    juego.laberinto = juego.matriz_a_cadena(mat)
    print(juego.laberinto)
    while True:
        if px == juego.posicion_final[0] and py == juego.posicion_final[1]:
            print("Felicidades, ganaste, eres el puto amo!!!!")
            break          
        else:
            print("Ingrese una tecla (w (arriba), a (izquierda), s (abajo) o d (derecha))")
            teclas = readchar.readkey()
            if teclas == 'w' or teclas == 'W':
                if px-1 >= 0 and mat[px-1][py] == '.':
                    mat[px][py] = '.'
                    px -= 1
            elif teclas == 'a' or teclas == 'A':
                if py-1 >= 0 and mat[px][py-1] == '.':
                    mat[px][py] = '.'
                    py -= 1
            elif teclas == 's' or teclas == 'S':
                if px+1 <= 20 and mat[px+1][py] == '.':
                    mat[px][py] = '.'
                    px += 1
            elif teclas == 'd' or teclas == 'D':
                if py+1 <= 20 and mat[px][py+1] == '.':
                    mat[px][py] = '.'
                    py += 1
            else:
                print("Ingrese una tecla válida")
            mat[px][py] = 'P'
            juego.limpiar_pantalla(mat)

main_loop(jugar)