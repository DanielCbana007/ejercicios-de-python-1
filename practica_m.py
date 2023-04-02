m = int(input("indique la cantidad de metros: "))

def yardas():
    return m*1.09361

def pulgadas():
    return m*39.3701

def pies():
    return m*3.28084

def centimetros():
    return m*100

print(f"metro: {m}\nyardas: {yardas()}\npulgadas: {pulgadas()}\npies: {pies()}\ncentimetros: {centimetros()}")