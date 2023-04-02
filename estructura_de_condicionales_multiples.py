# ejercicio1 

parcial = int(input("Nota del parcial: "))
final = int(input("Nota del final: "))
seguimiento = int(input("Nota del seguimiento: "))

resultado = ((parcial*20) + (final*30) + (seguimiento*50))/100
if(resultado > 4.5):
    print("desempeño Exelente")
elif(4.5 < resultado >= 4.0):
    print("desempeño Sobresaliente")
elif (3.9 <= resultado >= 3.0):
    print("desempeño Aceptable")
elif (resultado < 3.0):
    print("desempeño Insuficiente")
else:
    print("error")

# ejercicio2

numero1 = int(input("indique el numero1: "))
numero2 = int(input("indique el numero2: "))
numero3 = int(input("indique el numero3: "))

if (numero1 > numero2 & numero2 > numero3):
    print(f"{numero1} es mayor\n{numero2} es el numero del medio\n{numero3} es el numero menor")
elif (numero2 > numero1 & numero1 > numero3):
    print(f"{numero2} es mayor\n{numero1} es el numero del medio\n{numero3} es el numero menor")
elif (numero3 > numero2 & numero1 > numero2):
    print(f"{numero3} es mayor\n{numero1} es el numero del medio\n{numero2} es el numero menor")
elif(numero1 > numero3 & numero3 > numero2):
    print(f"{numero1} es mayor\n{numero3} es el numero del medio\n{numero2} es el numero menor")
elif(numero3 > numero1 & numero2 > numero1):
    print(f"{numero3} es mayor\n{numero2} es el numero del medio\n{numero1} es el numero menor")
elif(numero2 > numero3 & numero3 > numero1):
    print(f"{numero2} es mayor\n{numero3} es el numero del medio\n{numero1} es el numero menor")


# ejercicio 3

numero = int(input("escriba un numero que se encuentre edsde el 1 al 12: "))

if (numero == 1):
    print(f"el numero {numero} es corespondiente al mes de Enero")
elif (numero == 2):
    print(f"el numero {numero} es corespondiente al mes de Febrero")
elif (numero == 3):
    print(f"el numero {numero} es corespondiente al mes de Marzo")
elif (numero == 4):
    print(f"el numero {numero} es corespondiente al mes de Abril")
elif (numero == 5):
    print(f"el numero {numero} es corespondiente al mes de Mayo")
elif (numero == 6):
    print(f"el numero {numero} es corespondiente al mes de Junio")
elif (numero == 7):
    print(f"el numero {numero} es corespondiente al mes de Julio")
elif (numero == 8):
    print(f"el numero {numero} es corespondiente al mes de Agosto")
elif (numero == 9):
    print(f"el numero {numero} es corespondiente al mes de Septiembre")
elif (numero == 10):
    print(f"el numero {numero} es corespondiente al mes de Octubre")
elif (numero == 11):
    print(f"el numero {numero} es corespondiente al mes de Noviembre")
elif (numero == 12):
    print(f"el numero {numero} es corespondiente al mes de Diciembre")
else:
    print("error") 

# ejercicio 4

numero_horas_asistido = float(input("¿cuantas horas asistio al curso?: "))

horas_curso = 340

if (numero_horas_asistido < 70 % horas_curso):
    print("no aprobo")
elif (numero_horas_asistido >= 70 % horas_curso):
    print("aprobo")
else:
    print("error")

# ejercico 5

valor_compra = int(input("¿cuanto es el valor de su compra?:"))

if (valor_compra >= 60000):
    descuento = (valor_compra * 50)/100
    bono = 20 % valor_compra
    print(f"tienes un descuento de {descuento} pesos y un bono  de {bono} pesos")
elif (valor_compra >= 30000 & valor_compra <= 59999):
    descuento = (valor_compra * 15)/100
    print(f"tienes un descuento de {descuento} pesos")
elif (valor_compra >= 10000 & valor_compra <= 29999):
    descuento = (valor_compra * 5)/100
    print(f"tienes un descuento de {descuento} pesos")
else:
    print("error")


