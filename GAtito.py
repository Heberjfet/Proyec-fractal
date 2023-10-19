import tkinter as tk
from tkinter import messagebox

x_o = ["", "", "",
       "", "", "",
       "", "", ""]

victorias_x = 0
victorias_o = 0

gatos_ganados = [False] * 9

def crear_widgets():
    global etiqueta_jugador_actual, botones, simbolo_actual
    simbolo_actual = "X"
    colores = ["#ffcc80", "#b2dfdb", "#e6ee9c", "#ffe082", "#bcaaa4", "#ef9a9a", "#80cbc4", "#fff59d", "#90a4ae"]
    frame_jugador_actual = tk.Frame(raiz, bg="#cfd8dc")
    frame_jugador_actual.grid(row=0, column=0, columnspan=3)
    etiqueta_jugador_actual = tk.Label(frame_jugador_actual, text=f"Jugador Actual: {simbolo_actual}", bg="#cfd8dc", font=("Arial", 18))
    etiqueta_jugador_actual.pack(side=tk.LEFT, padx=10, pady=10)
    boton_reiniciar = tk.Button(frame_jugador_actual, text="Reiniciar", command=reiniciar_tablero)
    boton_reiniciar.pack(side=tk.RIGHT, padx=10, pady=10)
    botones = []
    for i in range(9):
        frame_boton = tk.Frame(raiz, bg=colores[i], borderwidth=2, relief=tk.RAISED)
        frame_boton.grid(row=i // 3 + 1, column=i % 3)
        grid_boton = tk.Frame(frame_boton, bg=colores[i])
        grid_boton.grid()
        fila_botones = []
        for j in range(9):
            boton = tk.Button(grid_boton, text=" ", width=2, height=1, bg=colores[i], command=lambda i=i, j=j: boton_presionado(i, j))
            boton.grid(row=j // 3, column=j % 3)
            fila_botones.append(boton)
        botones.append(fila_botones)
    raiz.configure(bg="#cfd8dc")
    
    # Desactivar el redimensionamiento de la ventana
    raiz.resizable(False, False)

def boton_presionado(fila, columna):
    global simbolo_actual
    boton = botones[fila][columna]
    if boton["text"] == " " and not gatos_ganados[fila]:
        boton["text"] = simbolo_actual
        ganador = revisar_ganador_tablero_0(fila)
        if ganador:
            etiqueta_jugador_actual["text"] = f"Ganó el jugador {ganador}!"
            gatos_ganados[fila] = True
            actualizar_contador(ganador)
        else:
            simbolo_actual = "O" if simbolo_actual == "X" else "X"
            etiqueta_jugador_actual["text"] = f"Jugador Actual: {simbolo_actual}"
        if all(gatos_ganados):
            determinar_ganador()

def revisar_ganador_tablero_0(row):
    simbolos = [botones[row][i]["text"] for i in range(9)]
    # Revisar filas
    for i in range(0, 9, 3):
        if simbolos[i] == simbolos[i + 1] == simbolos[i + 2] != " ":
            x_o[i] = simbolos[i]
            return simbolos[i]
    # Revisar columnas
    for i in range(3):
        if simbolos[i] == simbolos[i + 3] == simbolos[i + 6] != " ":
            x_o[i] = simbolos[i]
            return simbolos[i]
    # Revisar diagonales
    if simbolos[0] == simbolos[4] == simbolos[8] != " ":
        x_o[0] = simbolos[0]
        return simbolos[0]
    if simbolos[2] == simbolos[4] == simbolos[6] != " ":
        x_o[2] = simbolos[2]
        return simbolos[2]
    # Si no hay ganador, devolver None
    return None

def reiniciar_tablero():
    global simbolo_actual
    simbolo_actual = "X"
    etiqueta_jugador_actual["text"] = f"Jugador Actual: {simbolo_actual}"
    for fila in botones:
        for boton in fila:
            boton["text"] = " "
    for i in range(9):
        gatos_ganados[i] = False

def actualizar_contador(ganador):
    global victorias_x, victorias_o
    if ganador == "X":
        victorias_x += 1
    elif ganador == "O":
        victorias_o += 1

def determinar_ganador():
    global victorias_x, victorias_o
    if victorias_x > victorias_o:
        messagebox.showinfo("GANADOR", f"El ganador es el Jugador X con {victorias_x} victorias.")
    elif victorias_o > victorias_x:
        messagebox.showinfo("GANADOR", f"El ganador es el Jugador O con {victorias_o} victorias.")
    else:
        messagebox.showinfo("EMPATE", "El juego terminó en empate.")

raiz = tk.Tk()
crear_widgets()
raiz.mainloop()
