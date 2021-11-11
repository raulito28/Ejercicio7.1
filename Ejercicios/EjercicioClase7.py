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
"""lista coches"""
lista_coches
f_o = open("Coches.txt","w")
for coche in lista_coches:
    f_o.write(coche["Marca coche"]+","+coche["Modelo"]+","+\
              coche["Combustible"]+","+coche["Cilindrada"]+"\n")
f_o.close()
lista_coches =[]
c = open("Coches.txt","r")
for linea in c:
    coche = {}
    coche["Marca coche"],coche["Modelo"],coche["Combustible"],coche["Cilindrada"] = linea.split(",")
    lista_coches.append(coche)
print("Listado coches´: ",lista_coches)