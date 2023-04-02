x1 = float(input("Indique el valor de (x) del punto 1: \n"))
y1 = float(input("Indique el valor de (y) del punto 1: \n"))
x2 = float(input("Indique el valor de (x) del punto 2: \n"))
y2 = float(input("Indique el valor de (y) del punto 2: \n"))

def ecuasion():
    return float((y2-y1)/((x2-x1)))

print(f"la pendiente es {ecuasion()}")