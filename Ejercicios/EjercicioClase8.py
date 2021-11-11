lista_coches = []
while True:
    marca = input("Marca de coche: ")
    if marca == "fin":
        break
    modelo = input("Modelo: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    linea = {}
    linea["Marca coche"] = marca
    linea["Modelo"] = modelo
    linea["Combustible"] = combustible
    linea["Cilindrada"] = cilindrada
    lista_coches.append(linea)
for linea in lista_coches:
    print("Coche: ", linea)
""" picke lista coches """
import pickle

