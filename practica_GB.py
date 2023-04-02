GB = int(input("¿cuantos GB de almacenamiento dispone tu computador?:"))

def TB():
    return GB*0.00097656

def KB():
    return GB*1048576

print(f"GB: {GB}\nTB: {TB()}\nKB: {KB()}")