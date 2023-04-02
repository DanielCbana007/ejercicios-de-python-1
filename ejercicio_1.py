lado1 = int(input("Indique el valor de (a): "))
lado2 = int(input("Indique el valro de (b): "))

def perimetro(lado1,lado2):
    return (lado1 * 2) + (lado2 * 2)

def area(lado1, lado2):
    return lado1 * lado2 

print(f"el perimetro del rectangulo es {perimetro(lado1,lado2)} \nel area del rectangulo es {area(lado1,lado2)}")