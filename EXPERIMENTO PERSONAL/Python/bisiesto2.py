import tkinter as tk
from tkinter import Toplevel
from datetime import datetime, timedelta

# Función para calcular la edad
def calcular_edad():
    try:
        fecha_nacimiento_str = entry_fecha_nacimiento.get()
        
        # Validar que la fecha tenga el formato correcto
        if not validar_formato_fecha(fecha_nacimiento_str):
            label_error.config(text="Formato inválido. Usa DD/MM/AAAA.", fg="red")
            return
        
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
        fecha_actual = datetime.now()

        # Verificar si la fecha de nacimiento es en el futuro
        if fecha_nacimiento > fecha_actual:
            label_error.config(text="La fecha no puede estar en el futuro.", fg="red")
            return

        anio_nacimiento = fecha_nacimiento.year
        mes_nacimiento = fecha_nacimiento.month
        dia_nacimiento = fecha_nacimiento.day

        anio_actual = fecha_actual.year
        mes_actual = fecha_actual.month
        dia_actual = fecha_actual.day

        edad = anio_actual - anio_nacimiento

        if (mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento):
            edad -= 1

        cumple_este_anio = fecha_nacimiento.replace(year=anio_actual)
        dia_antes_cumple = cumple_este_anio - timedelta(days=1)
        dia_despues_cumple = cumple_este_anio + timedelta(days=1)

        # Mostrar el resultado dependiendo de la fecha
        if fecha_actual.date() == dia_antes_cumple.date():
            resultado = f"🎉 Mañana cumples {edad + 1} años. ¡Prepárate!"
            color_fondo = "#FFC300"
        elif fecha_actual.date() == dia_despues_cumple.date():
            resultado = f"🎁 Ayer fue tu cumpleaños. ¡Ahora tienes {edad} años!"
            color_fondo = "#F39C12"
        elif fecha_actual.date() == cumple_este_anio.date():
            resultado = f"🎂 ¡Feliz Cumpleaños! Hoy tienes {edad + 1} años. 🎈"
            color_fondo = "#58D68D"
        else:
            resultado = f"Actualmente tienes {edad} años."
            color_fondo = "#5DADE2"

        # Mostrar el resultado en un popup
        mostrar_resultado_popup(resultado, color_fondo)

    except ValueError:
        label_error.config(text="Por favor, ingresa una fecha válida en el formato DD/MM/AAAA.", fg="red")

# Validar el formato de la fecha (DD/MM/AAAA) y que solo contenga números
def validar_formato_fecha(fecha):
    if len(fecha) != 10:
        return False
    if not fecha[:2].isdigit() or not fecha[3:5].isdigit() or not fecha[6:].isdigit():
        return False
    if fecha[2] != "/" or fecha[5] != "/":
        return False
    return True

# Limpiar el texto de error al cambiar la entrada
def limpiar_error(event):
    label_error.config(text="")

# Restringir la entrada a solo números y el carácter "/"
def solo_numeros(event):
    char = event.char
    if char.isdigit() or char == "/":
        return
    return "break"

# Mostrar el resultado en un popup estilizado
def mostrar_resultado_popup(resultado, color_fondo):
    # Crear una nueva ventana Toplevel
    ventana_popup = Toplevel(root)
    ventana_popup.title("Resultado de Edad")
    ventana_popup.geometry("350x200")
    ventana_popup.configure(bg=color_fondo)

    # Título decorativo
    label_popup_titulo = tk.Label(ventana_popup, text="✨ Resultado ✨", font=("Comic Sans MS", 18, "bold"), bg=color_fondo, fg="white")
    label_popup_titulo.pack(pady=10)

    # Etiqueta con el resultado
    label_popup_resultado = tk.Label(ventana_popup, text=resultado, font=("Verdana", 14), bg=color_fondo, fg="white", wraplength=300, justify="center")
    label_popup_resultado.pack(pady=20)

    # Botón para cerrar el popup
    button_cerrar = tk.Button(ventana_popup, text="Cerrar", font=("Verdana", 12, "bold"), bg="white", fg=color_fondo, width=10, command=ventana_popup.destroy)
    button_cerrar.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Edad")
root.geometry("420x350")
root.configure(bg="#2C3E50")

# Estilos de la interfaz
font_title = ("Comic Sans MS", 20, "bold")
font_label = ("Verdana", 12)
font_button = ("Verdana", 12, "bold")

# Título con un pequeño ícono textual
label_title = tk.Label(root, text="🎂 Calculadora de Edad", font=font_title, bg="#2C3E50", fg="white")
label_title.pack(pady=15)

# Etiqueta para la fecha de nacimiento
label_fecha_nacimiento = tk.Label(root, text="Ingresa tu fecha de nacimiento (DD/MM/AAAA):", font=font_label, bg="#2C3E50", fg="white")
label_fecha_nacimiento.pack(pady=10)

# Cuadro de entrada para la fecha de nacimiento
entry_fecha_nacimiento = tk.Entry(root, font=font_label, justify='center', width=25, bd=2, relief="solid", bg="#ECF0F1")
entry_fecha_nacimiento.pack(pady=5)

# Evitar que se ingresen caracteres no numéricos
entry_fecha_nacimiento.bind("<KeyPress>", solo_numeros)

# Etiqueta de error
label_error = tk.Label(root, text="", font=("Verdana", 10), bg="#2C3E50", fg="white")
label_error.pack()

# Limpiar el error al escribir de nuevo
entry_fecha_nacimiento.bind("<Key>", limpiar_error)

# Botón para calcular la edad
button_calcular = tk.Button(root, text="Calcular Edad", font=font_button, bg="#1ABC9C", fg="white", command=calcular_edad, relief="flat", bd=5, width=20)
button_calcular.pack(pady=20)

# Pie de página con un icono de corazón
label_footer = tk.Label(root, text="HECHO CON ❤️ POR EQUIPO 3", font=font_label, bg="#2C3E50", fg="white")
label_footer.pack(side="bottom", pady=10)

# Iniciar la aplicación
root.mainloop()