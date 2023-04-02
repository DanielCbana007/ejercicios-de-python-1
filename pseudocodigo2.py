Peso = int(input("Indique su peso: "))

Estatura = float(input("Indique su estatura: ")) 

def masa_corporal(peso, altura):
    return (peso) / ((altura)**2)

print(f"Indice de masa corporal: {masa_corporal(Peso, Estatura)}")