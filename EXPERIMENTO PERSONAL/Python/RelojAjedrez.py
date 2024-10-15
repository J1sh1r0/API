import tkinter as tk
from tkinter import ttk
import time

# Variables globales
timer_white = 300
timer_black = 300
current_turn = 'white'
running = False
increment = 2
extra_time_active = False
last_move_time = time.time()
dark_mode = False

# Paleta de colores
light_bg_color = "#ecf0f1"
dark_bg_color = "#2c3e50"
light_fg_color = "#2c3e50"
dark_fg_color = "#ecf0f1"
button_color = "#e74c3c"
button_hover = "#c0392b"
active_color = "#27ae60"
timer_color_white = "#f39c12"
timer_color_black = "#3498db"

# Función para actualizar el reloj
def update_clock():
    global timer_white, timer_black, current_turn, running
    if running:
        if current_turn == 'white':
            timer_white -= 1
            time_left = format_time(timer_white)
            label_white.config(text=time_left)
        else:
            timer_black -= 1
            time_left = format_time(timer_black)
            label_black.config(text=time_left)

    if timer_white > 0 and timer_black > 0:
        root.after(1000, update_clock)

# Función para formatear el tiempo
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    return f"{minutes:02d}:{seconds:02d}"

# Función para cambiar de turno
def switch_turn():
    global current_turn, running, last_move_time
    if current_turn == 'white':
        current_turn = 'black'
    else:
        current_turn = 'white'
    running = True
    last_move_time = time.time()

# Función para finalizar el turno
def end_turn():
    global running, last_move_time
    running = False
    if extra_time_active:
        add_extra_time()
    switch_turn()

# Función para alternar el modo oscuro
def toggle_dark_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg=dark_bg_color)
        label_white.config(bg=dark_bg_color, fg=timer_color_white)
        label_black.config(bg=dark_bg_color, fg=timer_color_black)
        mode_button.config(bg=button_color, fg=dark_fg_color)
        extra_time_button.config(bg=button_color, fg=dark_fg_color)
        dark_mode_button.config(bg=button_color, fg=dark_fg_color)
        button_end_turn_white.config(bg=timer_color_white, fg=dark_fg_color)
        button_end_turn_black.config(bg=timer_color_black, fg=dark_fg_color)
        frame_top.config(bg=dark_bg_color)
    else:
        root.config(bg=light_bg_color)
        label_white.config(bg=light_bg_color, fg=timer_color_white)
        label_black.config(bg=light_bg_color, fg=timer_color_black)
        mode_button.config(bg=button_color, fg=light_fg_color)
        extra_time_button.config(bg=button_color, fg=light_fg_color)
        dark_mode_button.config(bg=button_color, fg=light_fg_color)
        button_end_turn_white.config(bg=timer_color_white, fg=light_fg_color)
        button_end_turn_black.config(bg=timer_color_black, fg=light_fg_color)
        frame_top.config(bg=light_bg_color)

# Función para alternar entre modos
def toggle_mode():
    global increment
    if mode_button.config('text')[-1] == 'Modo Normal':
        mode_button.config(text='Modo Competencia', bg=active_color)
        increment = 2
    else:
        mode_button.config(text='Modo Normal', bg=button_color)
        increment = 0

# Función para activar/desactivar tiempo extra
def toggle_extra_time():
    global extra_time_active
    extra_time_active = not extra_time_active
    if extra_time_active:
        extra_time_button.config(text="Tiempo Extra Activado", bg=active_color)
    else:
        extra_time_button.config(text="Tiempo Extra Desactivado", bg=button_color)

# Función para añadir tiempo extra
def add_extra_time():
    global timer_white, timer_black, current_turn, last_move_time
    current_time = time.time()
    elapsed_time = current_time - last_move_time
    if elapsed_time <= 5:
        reward_time = 3
    elif elapsed_time <= 10:
        reward_time = 2
    else:
        reward_time = 0

    if current_turn == 'white':
        timer_white += reward_time
        label_white.config(text=format_time(timer_white))
    else:
        timer_black += reward_time
        label_black.config(text=format_time(timer_black))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Chess Clock")
root.geometry("400x250")
root.config(bg=light_bg_color)

# Parte superior: botones de control
frame_top = tk.Frame(root, bg=light_bg_color)
frame_top.grid(row=0, column=0, columnspan=2, pady=10)

mode_button = ttk.Button(frame_top, text="Modo Normal", command=toggle_mode)
mode_button.grid(row=0, column=0, padx=10)

extra_time_button = ttk.Button(frame_top, text="Tiempo Extra Desactivado", command=toggle_extra_time)
extra_time_button.grid(row=0, column=1, padx=10)

dark_mode_button = ttk.Button(frame_top, text="Modo oscuro", command=toggle_dark_mode)
dark_mode_button.grid(row=0, column=2, padx=10)

# Relojes de los jugadores
label_white = tk.Label(root, text=format_time(timer_white), font=("Helvetica", 24), bg=light_bg_color, fg=timer_color_white)
label_white.grid(row=1, column=0, padx=20, pady=20)

label_black = tk.Label(root, text=format_time(timer_black), font=("Helvetica", 24), bg=light_bg_color, fg=timer_color_black)
label_black.grid(row=1, column=1, padx=20, pady=20)

# Botones "Turno terminado"
button_end_turn_white = tk.Button(root, text="Turno terminado", command=end_turn, bg=timer_color_white, fg=light_fg_color, font=("Helvetica", 12))
button_end_turn_white.grid(row=2, column=0, pady=10)

button_end_turn_black = tk.Button(root, text="Turno terminado", command=end_turn, bg=timer_color_black, fg=light_fg_color, font=("Helvetica", 12))
button_end_turn_black.grid(row=2, column=1, pady=10)

update_clock()

root.mainloop()
