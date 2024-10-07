import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

# Función para calcular la edad
def calcular_edad():
    try:
        # Obtener la fecha de nacimiento del campo de entrada
        fecha_nacimiento_str = entry_fecha_nacimiento.get()
        fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")
        
        fecha_actual = datetime.now()

        # Extraer el año, mes y día de las fechas proporcionadas
        anio_nacimiento = fecha_nacimiento.year
        mes_nacimiento = fecha_nacimiento.month
        dia_nacimiento = fecha_nacimiento.day

        anio_actual = fecha_actual.year
        mes_actual = fecha_actual.month
        dia_actual = fecha_actual.day

        # Calcular la edad
        edad = anio_actual - anio_nacimiento

        # Verificar si aún no ha cumplido años este año
        if (mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento):
            edad -= 1

        # Crear la fecha de cumpleaños para el año actual
        cumple_este_anio = fecha_nacimiento.replace(year=anio_actual)

        # Validación de si es el día anterior o posterior al cumpleaños
        dia_antes_cumple = cumple_este_anio - timedelta(days=1)
        dia_despues_cumple = cumple_este_anio + timedelta(days=1)

        # Mostrar el resultado
        if fecha_actual.date() == dia_antes_cumple.date():
            resultado = f"Aún tienes {edad}, mañana cumples {edad + 1} años."
        elif fecha_actual.date() == dia_despues_cumple.date():
            resultado = f"Ayer fue tu cumpleaños, ahora tienes {edad} años."
        elif fecha_actual.date() == cumple_este_anio.date():
            resultado = f"Hoy es tu cumpleaños, tienes {edad + 1} años."
        else:
            resultado = f"Tienes {edad} años."

        # Mostrar el resultado en una ventana emergente
        messagebox.showinfo("Resultado", resultado)
    
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa una fecha válida en el formato DD/MM/AAAA.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Edad")
root.geometry("400x300")
root.configure(bg="#2E4053")

# Estilos de la interfaz
font_title = ("Arial", 16, "bold")
font_label = ("Arial", 12)
font_button = ("Arial", 12, "bold")

# Título
label_title = tk.Label(root, text="Calculadora de Edad", font=font_title, bg="#2E4053", fg="white")
label_title.pack(pady=20)

# Etiqueta para la fecha de nacimiento
label_fecha_nacimiento = tk.Label(root, text="Ingresa tu fecha de nacimiento (DD/MM/AAAA):", font=font_label, bg="#2E4053", fg="white")
label_fecha_nacimiento.pack(pady=10)

# Cuadro de entrada para la fecha de nacimiento
entry_fecha_nacimiento = tk.Entry(root, font=font_label, justify='center', width=20)
entry_fecha_nacimiento.pack(pady=10)

# Botón para calcular la edad
button_calcular = tk.Button(root, text="Calcular Edad", font=font_button, bg="#1ABC9C", fg="white", command=calcular_edad)
button_calcular.pack(pady=20)

# Pie de página
label_footer = tk.Label(root, text="Hecho con ❤️ por [Tu Nombre]", font=font_label, bg="#2E4053", fg="white")
label_footer.pack(side="bottom", pady=10)

# Iniciar la aplicación
root.mainloop()