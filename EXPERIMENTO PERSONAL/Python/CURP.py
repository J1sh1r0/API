import tkinter as tk
from tkinter import messagebox
 
# Diccionario con claves de los estados
estados = {
    "AGUASCALIENTES": "AS", "BAJA CALIFORNIA": "BC", "BAJA CALIFORNIA SUR": "BS",
    "CAMPECHE": "CC", "COAHUILA": "CL", "COLIMA": "CM", "CHIAPAS": "CS", "CHIHUAHUA": "CH",
    "CIUDAD DE MEXICO": "DF", "DURANGO": "DG", "GUANAJUATO": "GT", "GUERRERO": "GR",
    "HIDALGO": "HG", "JALISCO": "JC", "MEXICO": "MC", "MICHOACAN": "MN", "MORELOS": "MS",
    "NAYARIT": "NT", "NUEVO LEON": "NL", "OAXACA": "OC", "PUEBLA": "PL", "QUERETARO": "QT",
    "QUINTANA ROO": "QR", "SAN LUIS POTOSI": "SP", "SINALOA": "SL", "SONORA": "SR",
    "TABASCO": "TC", "TAMAULIPAS": "TS", "TLAXCALA": "TL", "VERACRUZ": "VZ",
    "YUCATAN": "YN", "ZACATECAS": "ZS", "NACIDO EN EL EXTRANJERO": "NE"
}
 
# Función para reemplazar caracteres especiales
def reemplazar_caracteres(texto):
    return texto.replace('Ñ', 'X').replace('ñ', 'X')
 
# Función para obtener la primera vocal interna (excepto la primera letra)
def obtener_primera_vocal_interna(texto):
    for letra in texto[1:]:
        if letra in "AEIOU":
            return letra
    return "X"
 
# Función para obtener la primera consonante interna (excepto la primera letra)
def obtener_primera_consonante_interna(texto):
    for letra in texto[1:]:
        if letra in "BCDFGHJKLMNPQRSTVWXYZ":
            return letra
    return "X"
 
# Función para generar la CURP
def generar_curp():
    nombre = reemplazar_caracteres(entry_nombre.get().upper())
    primer_apellido = reemplazar_caracteres(entry_primer_apellido.get().upper())
    segundo_apellido = reemplazar_caracteres(entry_segundo_apellido.get().upper())
    fecha_nacimiento = entry_fecha_nacimiento.get()
    estado = entry_estado.get().upper()
    genero = entry_genero.get().upper()
 
    # Validación básica del estado
    if estado not in estados:
        messagebox.showerror("Error", "Estado no válido")
        return
 
    # Obtener la clave del estado
    clave_estado = estados[estado]
 
    # Generar la CURP
    curp = primer_apellido[0] + obtener_primera_vocal_interna(primer_apellido)
    curp += segundo_apellido[0] if segundo_apellido else "X"
    curp += nombre[0]
    curp += fecha_nacimiento[2:4] + fecha_nacimiento[5:7] + fecha_nacimiento[8:10]
    curp += genero
    curp += clave_estado
    curp += obtener_primera_consonante_interna(primer_apellido)
    curp += obtener_primera_consonante_interna(segundo_apellido) if segundo_apellido else "X"
    curp += obtener_primera_consonante_interna(nombre)
 
    # Mostrar la CURP en una nueva ventana
    ventana_resultado(curp)
 
# Función para crear una nueva ventana y mostrar la CURP generada
def ventana_resultado(curp):
    nueva_ventana = tk.Toplevel(root)
    nueva_ventana.title("CURP Generada")
   
    # Centrar la ventana
    center_window(nueva_ventana, 300, 150)
 
    tk.Label(nueva_ventana, text="Tu CURP es:", font=("Arial", 14)).pack(pady=10)
    tk.Label(nueva_ventana, text=curp, font=("Arial", 16, "bold")).pack(pady=10)
    tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack(pady=10)
 
# Función para centrar la ventana en la pantalla
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')
 
# Crear la interfaz gráfica principal
root = tk.Tk()
root.title("Generador CURP")
 
# Centrar la ventana principal
center_window(root, 400, 300)
 
# Entradas básicas
tk.Label(root, text="Nombre").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()
 
tk.Label(root, text="Primer apellido").pack()
entry_primer_apellido = tk.Entry(root)
entry_primer_apellido.pack()
 
tk.Label(root, text="Segundo apellido").pack()
entry_segundo_apellido = tk.Entry(root)
entry_segundo_apellido.pack()
 
tk.Label(root, text="Fecha de nacimiento (YYYY-MM-DD)").pack()
entry_fecha_nacimiento = tk.Entry(root)
entry_fecha_nacimiento.pack()
 
tk.Label(root, text="Estado de nacimiento").pack()
entry_estado = tk.Entry(root)
entry_estado.pack()
 
tk.Label(root, text="Género (H/M)").pack()
entry_genero = tk.Entry(root)
entry_genero.pack()
 
# Botón para generar la CURP
tk.Button(root, text="Generar CURP", command=generar_curp).pack(pady=10)
 
# Iniciar la aplicación
root.mainloop()