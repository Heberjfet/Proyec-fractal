import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configurar la ventana
size = width, height = 600, 600
screen = pygame.display.set_mode(size)

# Configurar los colores
white = (255, 255, 255)
line_color = (0, 0, 0)

# Configurar el tablero
board = [[None]*9 for _ in range(9)]

# Dibujar el tablero
def draw_board():
    # Dibujar el fondo
    screen.fill(white)

    # Dibujar las líneas verticales y horizontales
    for i in range(1, 9):
        pygame.draw.line(screen, line_color, (i * width // 9, 0), (i * width // 9, height), 2)
        pygame.draw.line(screen, line_color, (0, i * height // 9), (width, i * height // 9), 2)

# Verificar si hay un ganador
def check_win(board):
    # Verificar las filas y columnas
    for i in range(9):
        if all_same(board[i]) or all_same([board[j][i] for j in range(9)]):
            return True

    # Verificar las diagonales
    if all_same([board[i][i] for i in range(9)]) or all_same([board[i][8 - i] for i in range(9)]):
        return True

    return False

# Verificar si todos los elementos de una lista son iguales y no nulos
def all_same(lst):
    return lst.count(lst[0]) == len(lst) and lst[0] is not None

# Bucle principal del juego
def game_loop():
    running = True
    player = "X"

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obtener la posición del mouse
                mouseX = event.pos[0] 
                mouseY = event.pos[1]

                # Calcular la fila y columna del tablero
                row = int(mouseY // (height / 9))
                col = int(mouseX // (width / 9))

                # Marcar el espacio en el tablero si está vacío
                if board[row][col] is None:
                    board[row][col] = player

                    # Cambiar de jugador si no hay un ganador aún
                    if not check_win(board):
                        player = "O" if player == "X" else "X"
                    else:
                        print("¡El jugador", player, "ha ganado!")
                        running = False

        draw_board()
        pygame.display.update()

    pygame.quit()
    sys.exit()

game_loop()

