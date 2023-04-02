Nombre =input("Indique su nombre: ")
Dia = int(input("Indique su dia de nacimiento: ")) 
Mes = int(input("Indique su mes de nacimiento: ")) 
year = int(input("Indique su año de nacimiento: ")) 
Celular = int(input("Indique su numero telefonico: ")) 
Correo = input("Indique su correo: ")
Manzana = input("Indique su la manzana en donde vive: ") 
Lote = input("Indique el lote en donde vive: ")  
Barrio = input("Indique el barrio en donde vive: ") 

def fecha_de_nacimiento():
    return (f"{Dia}/{Mes}/{year}")

def años():
    return 2023 - year

def vivienda():
    return(f"{Manzana}/{Lote}/{Barrio}")

print(f"Tu nombre es: {Nombre} \nTu dia de nacimiento es {fecha_de_nacimiento()} \nTu numero de telefono es:{Celular} \nTu correo es: {Correo} \nVives en:{vivienda()} \n tienes {años()}")