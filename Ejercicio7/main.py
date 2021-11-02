lista_telefono = list()

while True:
    nombre = input("Nombre del contacto: ")
    if nombre == "fin":
        break
    telefono = input("Número de teléfono: ")

    linea = {}
    linea["Nombre"] = nombre
    linea["Nmero de teléfono"] = telefono

    lista_telefono.append(linea)

print("Lista numeros d etelfono: \n", lista_telefono)