# ejercicio1

parcial = int(input("Nota del parcial: "))
final = int(input("Nota del final: "))
seguimiento = int(input("Nota del seguimiento: "))

def algoritmo(parcial, final, seguimiento):
    resultado = ((parcial*20) + (final*30) + (seguimiento*50))/100
    if(resultado >= 3):
        print("aprobo")
    elif(resultado < 3):
        print("no aprobo")
    else:
        print("error")

# ejercicio2

horas_tabajadas = int(input("¿cuantas horas trabajo?: "))
salario_horas = int(input("¿cuanto gna por hora?: "))

def sueldo():
    if(horas_tabajadas > 40):
       return horas_tabajadas * (salario_horas * 2)
    else:
       return horas_tabajadas * salario_horas
    
print(f"su sueldo es de {sueldo}")

# ejercicio3

numero = int(input("indique un numero: "))

if(numero > 0 ):
    print(f"el numero {numero} es positivo")
else:
    print(f"el numero { numero} es negativo")

# ejercicio4

numero1 = int(input("indique el numero1: "))
numero2 = int(input("indique el numero2: "))

if(numero1 > 0 & numero2 <= 0):
    print(f"{numero1} es positivo y {numero2} es negativo")
elif (numero2 > 0 & numero1 <= 0):
    print(f"{numero2} es positivo y {numero1} es negativo")
else:
    print("los numero son iguales")

# ejercicio5

nombre = [input("escrive tu nombre: ").lower()]

if (nombre[0] == "a", "e", "i", "o"):
    print("tun nombre empieza con vocal")
else:
    print(f"tu nombre no empieza con vocal, empieza con: {nombre[0]}")

# ejercicio 4