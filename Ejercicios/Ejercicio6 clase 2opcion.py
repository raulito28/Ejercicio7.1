def contar_vocales(palabra):
    contador = 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            contador += 1
    return contador

palabra = input("Dime una palabra: ")
cantidad = contar_vocales(palabra)
print(f"En la palabra '{palabra}'' hay {cantidad} vocales")