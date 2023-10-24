#Parte 4, laberinto

import os, readchar

laberinto = """..###################
..............#...#.#
###.#.###.#####.#.#.#
#.#.#.#...#.....#...#
#.#####.###.###.#####
#.....#.......#.#...#
###.#.#.#.#######.#.#
#...#...#.#.......#.#
#.#####.#####.#######
#.#.........#.......#
###.#########.###.###
#...........#...#.#.#
#.#####.###.#.#.###.#
#.....#.#.#...#.....#
#.#.#####.###.#.#####
#.#.......#.#.#.#...#
#.#.###.###.#####.###
#.#.#...#.#.#.....#.#
#.###.#.#.#.###.#.#.#
#...#.#.........#...#
###################.#"""

def conv_matriz(cadena):
    matriz = cadena.split("\n")
    for i in range(len(matriz)):
        matriz[i] = list(matriz[i])
    return matriz
    
def limpiar_pantalla(mat):
    os.system('cls' if os.name=='nt' else 'clear')
    laberinto = matriz_a_cadena(mat)
    print(laberinto)

def matriz_a_cadena(matriz):
    cadena_laberinto = "\n".join(["".join(fila) for fila in matriz])
    return cadena_laberinto

matriz_conv = conv_matriz(laberinto)

posicion_inicial = (0,0)
posicion_final = (20,19)

def main_loop(mat, pos_ini, pos_fin):
    px = pos_ini[0]
    py = pos_ini[1]
    mat[px][py] = 'P'
    laberinto = matriz_a_cadena(mat)
    print(laberinto)
    while True:
        if px == pos_fin[0] and py == pos_fin[1]:
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
            limpiar_pantalla(mat)
            
main_loop(matriz_conv, posicion_inicial, posicion_final)