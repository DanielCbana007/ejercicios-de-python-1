partidosganados = int(input("indique cuantos partidos ganó: "))
partidosempatados = int(input("indique cuantos partidos empató: "))

def puntos_totales():
    return (partidosganados*3) + (partidosempatados*1)    

print(f"tienes {puntos_totales()} puntos")