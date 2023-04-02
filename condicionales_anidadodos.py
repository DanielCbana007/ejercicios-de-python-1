# ejercico 1

ingreso = int(input("si es estudiante escriba 1, si es docente escriba 2, si es administrador escriba 3, escriva otra cosa si no es ninguno de los anteriores: "))


if(ingreso == 1):
    codigo = int(input("ingrese su codigo de estudiante: "))
    print(f"bienvenido su codigo es: {codigo}")
elif(ingreso == 2 | ingreso == 3):
    documento = input("ingrese su tipo de documento: ")
    print(f"bienvenido, su documento es: {documento}")
else:
    nombre = input("ingrese su nombre: ")
    apellido = input("ingrese su apellido: ")
    documento = int(input("ingrese su numero de documento: "))
    print(f"bienvenido{nombre} {apellido} su documento es:{documento}")

# ejercicio 2

ingreso = int(input("si quiere jugo escriba 1, si quiere panserotti escriba 2, si quiere pizza escriba 3: "))
unidasdes = int(input("¿cuantas unidades quiere?:"))


precio_jugo = 2000
precio_panserotti = 3500
precio_pizza = 6000

if (ingreso == 1 ):
    if(unidasdes >= 2):
        print((precio_jugo * unidasdes) - 0.1)
    elif(unidasdes == 1):
        print(precio_jugo)
    else:
        print("error")
elif (ingreso == 2 ):
    if(unidasdes > 2):
        print((precio_panserotti * unidasdes) - 0.15)
    elif(unidasdes <= 2):
        print(precio_panserotti)
    else:
        print("error")
elif(ingreso == 3):
    if (unidasdes == 2):
        print((precio_pizza * unidasdes) - 0.1)
    elif(unidasdes > 5):
        print((precio_pizza * unidasdes) - 0.3)  
    else:
        print("error")
else:
        print("error")
    
# ejercicio 3

mezclar_colores = int(input("para mezclar colores primarios escriba 1, para mezclar colores primarios y secundarios esciba 2:"))
colores_primarios = ["Amarillo", "Rojo", "azul"]
colores_secundarios =["Naranja", "Verde", "Morado"]
otoro_color = "turquesa"

if (mezclar_colores == 1):
    print(f"{colores_primarios[0]} + {colores_primarios [2]} = {colores_secundarios[2]}")
elif (mezclar_colores == 2):
    print(f"Su mezcla de colores primarios y secundarios ha dado como resultado el {otoro_color}")

# ejercicio 4

tipo_de_bus = int(input("que tipo de bus necesita, para un bus grande escriba 1, para un bus mediano escriba 2, para una buseta escriba 3: "))
numero_estudiantes = int(input("escriba cuantos estudiantes van en el bus: "))

if (tipo_de_bus == 1):
    if (numero_estudiantes == 40):
        print("el bus es ideal para el viaje")
    elif (tipo_de_bus > 40):
        print("necesita mas de un bus")
    elif (40 < numero_estudiantes > 35):
        print("el bus tiene suficiente espacio")
elif (tipo_de_bus == 2):
    if (numero_estudiantes == 35):
        print("el bus es ideal para el viaje")
    elif (tipo_de_bus > 35):
        print("necesita mas de un bus o un bus mas grande")
    elif (35 < numero_estudiantes > 24):
        print("el bus tiene suficiente espacio")
elif (tipo_de_bus == 3):
    if (numero_estudiantes == 24):
        print("el bus es ideal para el viaje")
    elif (tipo_de_bus > 24):
        print("necesita mas de un bus o un bus mas grande")
    elif (24 < numero_estudiantes >= 1):
        print("el bus tiene suficiente espacio")
    else:
        print("no necesita buses")
else:
    print("error")

# ejercico 5

tipo_procesador = int(input("escriba 1 para Ryzen y escriba 2 para Intel: "))

if (tipo_procesador == 1):
    referencia = ("indique la referencia del procesador: ")
    if (referencia == "Ryzen 3 4100"):
        print(f"el valor en pesos colombianos es {66.11 * 0.00022}")
    elif (referencia == "Ryzen 5 4500"):
        print(f"el valor en pesos colombianos es {80.98 * 0.00022}")
    elif (referencia == "Ryzen 7 7700"):
        print(f"el valor en pesos colombianos es {360.36 * 0.00022}")
    elif (referencia == "Ryzen 9 7900"):
        print(f"el valor en pesos colombianos es {490.90 * 0.00022}")
    else:
        print("error")
elif ():
    referencia = ("indique la referencia del procesador: ")
    if (referencia == "Core i3-10100"):
        print(f"el valor en pesos colombianos es {94.49 * 0.00022}")
    elif (referencia == "Core i5-13500"):
        print(f"el valor en pesos colombianos es {273.38 * 0.00022}")
    elif (referencia == "Core i7-13700"):
        print(f"el valor en pesos colombianos es {395.01 * 0.00022}")
    else:
        print("error")
else:
    print("error")