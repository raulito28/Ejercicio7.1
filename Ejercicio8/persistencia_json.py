def store():
    import json
    lista_coches = json.load(open("Coches.txt", "r"))
    while True:
        coche = {}
        marca = input("Marca de coche: ")
        if marca == "fin":
            break
        coche["Marca Coche"] = marca
        coche["Modelo"] = input("Modelo: ")
        coche["Combustible"] = input("Combustible: ")
        coche["Cilindrada"] = input("Cilindrada: ")
        lista_coches.append(coche)

    for coche in lista_coches:
        print("Coche: ", coche)
def retrieve():
    return ["Coches.txt"]