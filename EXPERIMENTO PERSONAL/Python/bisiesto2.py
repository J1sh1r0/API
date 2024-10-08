import tkinter as tk  # Importa la librería tkinter para crear interfaces gráficas.
from tkinter import Toplevel  # Importa Toplevel para crear ventanas emergentes (popups).
from datetime import datetime, timedelta  # Importa datetime y timedelta para trabajar con fechas.

# Función para calcular la edad
def calcular_edad():
    try:
        # Obtiene la fecha de nacimiento como string desde el campo de entrada.
        fecha_nacimiento_str = entry_fecha_nacimiento.get()
        
        # Verifica si el formato de la fecha es correcto usando la función validar_formato_fecha.
        if not validar_formato_fecha(fecha_nacimiento_str):
            # Si el formato es inválido, muestra un mensaje de error en la etiqueta de error.
            label_error.config(text="Formato inválido. Usa DD/MM/AAAA.", fg="red")
            return
        
        # Convierte la fecha ingresada a un objeto datetime.
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
        fecha_actual = datetime.now()  # Obtiene la fecha y hora actual.

        # Verifica si la fecha de nacimiento ingresada es en el futuro.
        if fecha_nacimiento > fecha_actual:
            # Si es en el futuro, muestra un mensaje de error en la etiqueta de error.
            label_error.config(text="La fecha no puede estar en el futuro.", fg="red")
            return

        # Extrae el año, mes y día de la fecha de nacimiento.
        anio_nacimiento = fecha_nacimiento.year
        mes_nacimiento = fecha_nacimiento.month
        dia_nacimiento = fecha_nacimiento.day

        # Extrae el año, mes y día de la fecha actual.
        anio_actual = fecha_actual.year
        mes_actual = fecha_actual.month
        dia_actual = fecha_actual.day

        # Calcula la edad inicial restando los años.
        edad = anio_actual - anio_nacimiento

        # Verifica si la persona aún no ha cumplido años este año.
        if (mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento):
            # Si no ha cumplido, resta un año.
            edad -= 1

        # Calcula la fecha de cumpleaños para el año actual.
        cumple_este_anio = fecha_nacimiento.replace(year=anio_actual)
        # Calcula el día anterior al cumpleaños.
        dia_antes_cumple = cumple_este_anio - timedelta(days=1)
        # Calcula el día posterior al cumpleaños.
        dia_despues_cumple = cumple_este_anio + timedelta(days=1)

        # Verifica en qué día se encuentra el usuario con respecto a su cumpleaños.
        if fecha_actual.date() == dia_antes_cumple.date():
            # Si es el día anterior al cumpleaños.
            resultado = f"🎉 Mañana cumples {edad + 1} años. ¡Prepárate!"
            color_fondo = "#FFC300"  # Color de fondo amarillo.
        elif fecha_actual.date() == dia_despues_cumple.date():
            # Si es el día posterior al cumpleaños.
            resultado = f"🎁 Ayer fue tu cumpleaños. ¡Ahora tienes {edad} años!"
            color_fondo = "#F39C12"  # Color de fondo naranja.
        elif fecha_actual.date() == cumple_este_anio.date():
            # Si es el día del cumpleaños.
            resultado = f"🎂 ¡Feliz Cumpleaños! Hoy tienes {edad + 1} años. 🎈"
            color_fondo = "#58D68D"  # Color de fondo verde.
        else:
            # Si no es un día cercano al cumpleaños.
            resultado = f"Actualmente tienes {edad} años."
            color_fondo = "#5DADE2"  # Color de fondo azul.

        # Muestra el resultado en un popup estilizado.
        mostrar_resultado_popup(resultado, color_fondo)

    except ValueError:
        # Maneja el error si se ingresa una fecha inválida.
        label_error.config(text="Por favor, ingresa una fecha válida en el formato DD/MM/AAAA.", fg="red")

# Función para validar que la fecha tenga el formato correcto (DD/MM/AAAA).
def validar_formato_fecha(fecha):
    if len(fecha) != 10:
        return False
    # Verifica que las partes correspondientes a día, mes y año sean numéricas.
    if not fecha[:2].isdigit() or not fecha[3:5].isdigit() or not fecha[6:].isdigit():
        return False
    # Verifica que los caracteres en las posiciones 3 y 6 sean "/".
    if fecha[2] != "/" or fecha[5] != "/":
        return False
    return True

# Función para limpiar el mensaje de error al modificar la entrada.
def limpiar_error(event):
    label_error.config(text="")

# Restringe la entrada del teclado a solo números y el carácter "/".
def solo_numeros(event):
    char = event.char
    if char.isdigit() or char == "/":
        return
    return "break"

# Función para mostrar el resultado en un popup estilizado.
def mostrar_resultado_popup(resultado, color_fondo):
    # Crea una nueva ventana popup.
    ventana_popup = Toplevel(root)
    ventana_popup.title("Resultado de Edad")  # Título del popup.
    ventana_popup.geometry("350x200")  # Tamaño del popup.
    ventana_popup.configure(bg=color_fondo)  # Color de fondo del popup.

    # Etiqueta de título decorativa en el popup.
    label_popup_titulo = tk.Label(ventana_popup, text="✨ Resultado ✨", font=("Comic Sans MS", 18, "bold"), bg=color_fondo, fg="white")
    label_popup_titulo.pack(pady=10)

    # Etiqueta con el resultado en el popup.
    label_popup_resultado = tk.Label(ventana_popup, text=resultado, font=("Verdana", 14), bg=color_fondo, fg="white", wraplength=300, justify="center")
    label_popup_resultado.pack(pady=20)

    # Botón para cerrar el popup.
    button_cerrar = tk.Button(ventana_popup, text="Cerrar", font=("Verdana", 12, "bold"), bg="white", fg=color_fondo, width=10, command=ventana_popup.destroy)
    button_cerrar.pack(pady=10)

# Crea la ventana principal de la aplicación.
root = tk.Tk()
root.title("Calculadora de Edad")  # Título de la ventana principal.
root.geometry("420x350")  # Tamaño de la ventana principal.
root.configure(bg="#2C3E50")  # Color de fondo de la ventana principal.

# Estilos para los elementos de la interfaz.
font_title = ("Comic Sans MS", 20, "bold")  # Fuente para el título.
font_label = ("Verdana", 12)  # Fuente para las etiquetas.
font_button = ("Verdana", 12, "bold")  # Fuente para los botones.

# Título principal con un ícono textual.
label_title = tk.Label(root, text="🎂 Calculadora de Edad", font=font_title, bg="#2C3E50", fg="white")
label_title.pack(pady=15)

# Etiqueta para pedir la fecha de nacimiento.
label_fecha_nacimiento = tk.Label(root, text="Ingresa tu fecha de nacimiento (DD/MM/AAAA):", font=font_label, bg="#2C3E50", fg="white")
label_fecha_nacimiento.pack(pady=10)

# Campo de entrada para la fecha de nacimiento.
entry_fecha_nacimiento = tk.Entry(root, font=font_label, justify='center', width=25, bd=2, relief="solid", bg="#ECF0F1")
entry_fecha_nacimiento.pack(pady=5)

# Evitar que se ingresen caracteres no numéricos o el carácter "/".
entry_fecha_nacimiento.bind("<KeyPress>", solo_numeros)

# Etiqueta para mostrar mensajes de error.
label_error = tk.Label(root, text="", font=("Verdana", 10), bg="#2C3E50", fg="white")
label_error.pack()

# Limpiar el mensaje de error al cambiar el texto del campo de entrada.
entry_fecha_nacimiento.bind("<Key>", limpiar_error)

# Botón para calcular la edad.
button_calcular = tk.Button(root, text="Calcular Edad", font=font_button, bg="#1ABC9C", fg="white", command=calcular_edad, relief="flat", bd=5, width=20)
button_calcular.pack(pady=20)

# Pie de página con un mensaje personalizado.
label_footer = tk.Label(root, text="HECHO CON ❤️ POR EQUIPO 3", font=font_label, bg="#2C3E50", fg="white")
label_footer.pack(side="bottom", pady=10)

# Iniciar el bucle principal de la aplicación.
root.mainloop()