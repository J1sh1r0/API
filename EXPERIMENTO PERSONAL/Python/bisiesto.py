import tkinter as tk  # Se importa la librería tkinter para crear la interfaz gráfica.
from tkinter import messagebox  # Se importa messagebox para mostrar mensajes emergentes.
from datetime import datetime, timedelta  # Se importan datetime y timedelta para trabajar con fechas.

# Función para calcular la edad
def calcular_edad():
    try:
        # Obtener la fecha de nacimiento del campo de entrada (input del usuario)
        fecha_nacimiento_str = entry_fecha_nacimiento.get()
        # Convertir la fecha ingresada (en formato DD/MM/AAAA) a un objeto datetime
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
        
        # Obtener la fecha actual
        fecha_actual = datetime.now()

        # Extraer el año, mes y día de la fecha de nacimiento
        anio_nacimiento = fecha_nacimiento.year
        mes_nacimiento = fecha_nacimiento.month
        dia_nacimiento = fecha_nacimiento.day

        # Extraer el año, mes y día de la fecha actual
        anio_actual = fecha_actual.year
        mes_actual = fecha_actual.month
        dia_actual = fecha_actual.day

        # Calcular la edad inicial restando los años
        edad = anio_actual - anio_nacimiento

        # Verificar si la persona aún no ha cumplido años este año
        if (mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento):
            edad -= 1  # Si no ha cumplido, se resta un año a la edad

        # Crear la fecha de cumpleaños para el año actual
        cumple_este_anio = fecha_nacimiento.replace(year=anio_actual)

        # Calcular el día anterior y el día posterior al cumpleaños
        dia_antes_cumple = cumple_este_anio - timedelta(days=1)
        dia_despues_cumple = cumple_este_anio + timedelta(days=1)

        # Mostrar el resultado dependiendo de la fecha actual
        if fecha_actual.date() == dia_antes_cumple.date():
            # Si hoy es el día antes del cumpleaños
            resultado = f"Aún tienes {edad}, mañana cumples {edad + 1} años."
        elif fecha_actual.date() == dia_despues_cumple.date():
            # Si hoy es el día después del cumpleaños
            resultado = f"Ayer fue tu cumpleaños, ahora tienes {edad} años."
        elif fecha_actual.date() == cumple_este_anio.date():
            # Si hoy es el día de su cumpleaños
            resultado = f"Hoy es tu cumpleaños, tienes {edad + 1} años."
        else:
            # Si no es un día cercano al cumpleaños
            resultado = f"Tienes {edad} años."

        # Mostrar el resultado en una ventana emergente
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        # Manejo de error si se ingresa una fecha en formato incorrecto
        messagebox.showerror("Error", "Por favor, ingresa una fecha válida en el formato DD/MM/AAAA.")

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Calculadora de Edad")  # Título de la ventana
root.geometry("400x300")  # Tamaño de la ventana
root.configure(bg="#2E4053")  # Color de fondo de la ventana

# Estilos de las fuentes (tipos de letra) a usar en los textos
font_title = ("Arial", 16, "bold")  # Fuente para el título
font_label = ("Arial", 12)  # Fuente para las etiquetas
font_button = ("Arial", 12, "bold")  # Fuente para los botones

# Título principal de la aplicación
label_title = tk.Label(root, text="Calculadora de Edad", font=font_title, bg="#2E4053", fg="white")
label_title.pack(pady=20)  # Agregar el título a la ventana con un espacio vertical de 20 píxeles

# Etiqueta que solicita la fecha de nacimiento al usuario
label_fecha_nacimiento = tk.Label(root, text="Ingresa tu fecha de nacimiento (DD/MM/AAAA):", font=font_label, bg="#2E4053", fg="white")
label_fecha_nacimiento.pack(pady=10)  # Agregar la etiqueta a la ventana con 10 píxeles de espacio

# Campo de entrada para que el usuario ingrese su fecha de nacimiento
entry_fecha_nacimiento = tk.Entry(root, font=font_label, justify='center', width=20)
entry_fecha_nacimiento.pack(pady=10)  # Colocar el campo de entrada con 10 píxeles de espacio

# Botón para calcular la edad cuando se presiona
button_calcular = tk.Button(root, text="Calcular Edad", font=font_button, bg="#1ABC9C", fg="white", command=calcular_edad)
button_calcular.pack(pady=20)  # Colocar el botón en la ventana con 20 píxeles de espacio

# Pie de página con un mensaje personalizado
label_footer = tk.Label(root, text="HECHO CON ❤️ POR EQUIPO 3", font=font_label, bg="#2E4053", fg="white")
label_footer.pack(side="bottom", pady=10)  # Colocar el pie de página en la parte inferior de la ventana

# Iniciar el bucle principal de la aplicación
root.mainloop()
