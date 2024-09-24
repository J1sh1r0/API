from datetime import datetime, timedelta

def calcular_edad(fecha_nacimiento, fecha_actual):
    # Extraemos el año, mes y día de las fechas proporcionadas
    anio_nacimiento = fecha_nacimiento.year
    mes_nacimiento = fecha_nacimiento.month
    dia_nacimiento = fecha_nacimiento.day

    anio_actual = fecha_actual.year
    mes_actual = fecha_actual.month
    dia_actual = fecha_actual.day

    # Calculamos la edad
    edad = anio_actual - anio_nacimiento

    # Verificamos si aún no ha cumplido años este año
    if (mes_actual, dia_actual) < (mes_nacimiento, dia_nacimiento):
        edad -= 1

    # Crear la fecha de cumpleaños para el año actual
    cumple_este_anio = fecha_nacimiento.replace(year=anio_actual)

    # Validación de si es el día anterior o posterior al cumpleaños
    dia_antes_cumple = cumple_este_anio - timedelta(days=1)
    dia_despues_cumple = cumple_este_anio + timedelta(days=1)

    # Comprobamos el día actual
    if fecha_actual.date() == dia_antes_cumple.date():
        print(f"Aún tienes {edad}, mañana cumples {edad + 1} años.")
    elif fecha_actual.date() == dia_despues_cumple.date():
        print(f"Ayer fue tu cumpleaños, ahora tienes {edad} años.")
    elif fecha_actual.date() == cumple_este_anio.date():
        print(f"Hoy es tu cumpleaños, tienes {edad + 1} años.")
    else:
        print(f"Tienes {edad} años.")

# Capturar fecha de nacimiento
fecha_nacimiento_str = input("Ingresa tu fecha de nacimiento (DD/MM/AAAA): ")
fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")

# Capturar la fecha actual (tecleada por el usuario)
fecha_actual_str = input("Ingresa la fecha actual (DD/MM/AAAA): ")
fecha_actual = datetime.strptime(fecha_actual_str, "%d/%m/%Y")

calcular_edad(fecha_nacimiento, fecha_actual)
