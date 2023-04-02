# ejercicio 1

numero1 = int(input("Indique el un numero1: "))
numero2 = int(input("Indique el un numero2: "))

def suma():
    return numero1 + numero2

def multiplicacion():
    return numero1 * numero2

print(f"el resultado de la suma es: {suma()}\nel resultado de la suma es: {multiplicacion()}")

# ejercicio 2

horas_valor = int(input("Indique el valor de la hora: "))
numero_horas = int(input("Indique el numero de horas: "))

def salario_neto():
    return (numero_horas * horas_valor)/0.16


print(f"el salario neto es de: {salario_neto()}")

# ejercico 3

trasporte =  int(input("Indique el valor del trasporte: "))
hospedaje =  int(input("Indique el valor del hospedaje: "))
alimentacion =  int(input("Indique el valor de la alimentacion: "))

def valor_total():
    return trasporte + horas_valor + alimentacion

print(f"el valor total del tour es de: {valor_total()}")

# ejercicio 4

pesos_colombianos = int(input("Indique el valor de pesos colombianos: "))

def dolar():
    return pesos_colombianos *4.813,43

def euro():
    return pesos_colombianos *5.183,39

def peso_mexicano():
    return pesos_colombianos *258,66

def libra_esterlina():
    return pesos_colombianos *5.879,60

def sol_peruano():
    return pesos_colombianos *1.274,59
print(f"el valor en pesos colombianos es: {pesos_colombianos}\npeso colombiano a dolar: {dolar()} \npeso colombiano a euro: {euro()} \npeso colombiano a peso mexicano: {peso_mexicano()} \npeso colombiano a libra esterlina: {libra_esterlina()} \npeso colombiano a sol peruano: {sol_peruano()} \n")