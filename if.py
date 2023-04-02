"""# ejercicio1

numero1 = int(input("Indique el numero1:"))
numero2 = int(input("Indique el numero2:"))

if(numero1 > numero2):
    print(f"{numero1} es mayor que {numero2}")
elif(numero1 == numero2):
    print("los numeros son iguales")
else:
    print(f"{numero1} es menor que {numero2}")

# ejercicio2

horas_valor = int(input("Indique el valor de la hora: "))
numero_horas = int(input("Indique el numero de horas: "))

def salario_neto():
    salario = (numero_horas * horas_valor)

    if(salario <= 2000000):
        return 16 % salario 
    else:
        return 24 % salario


print(f"el salario neto es de: {salario_neto()}")

# ejercicio3

trasporte =  int(input("Indique el valor del trasporte: "))
hospedaje =  int(input("Indique el valor del hospedaje: "))
alimentacion =  int(input("Indique el valor de la alimentacion: "))
avion = int("¿viajara en avion?")

def valor_total():
    if(avion == "si"):
        return trasporte + horas_valor + alimentacion + 500000
    else:
        return trasporte + horas_valor + alimentacion


print(f"el valor total del tour es de: {valor_total()}")"""

# ejercicio4

Peso = int(input("Indique su peso: "))
Estatura = float(input("Indique su estatura: ")) 


if((Peso) / (Estatura**2) < 18.5):
        print("por debajo")
elif((Peso) / (Estatura**2) > 18.5 and (Peso) / (Estatura**2)< 24.9):
        print("saludable")
elif((Peso) / (Estatura**2) > 25 and (Peso) / (Estatura**2)< 29.9): 
        print("sobrepeso")
elif((Peso) / (Estatura**2) > 30 and (Peso) / (Estatura**2)< 34.9):
        print("obesidad I")
elif((Peso) / (Estatura**2) > 35 and (Peso) / (Estatura**2)< 39.9):
        print("obesidad II")
elif((Peso) / (Estatura**2) > 40):
        print("obesidad III")  
         

# ejercicio5
"""
temperatura = int(input("indique la temperatura en °C: "))

def F():
    return (temperatura * (9/5)) + 32 

def K():
    return temperatura + 273.15

print(f"la temperatura de °C a °F es: {F()}\nla temperatura de °C a °K es: {K()}")

# ejercicio6

numero = int(input("escriva un numero: "))

if(numero < 0):
    print(f"el numero {numero} es negativo")
elif(numero == 0):
    print(f"el numero {numero} es cero")
else:
    print(f"el numero {numero} es positivo")"""