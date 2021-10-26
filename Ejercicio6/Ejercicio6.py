import statistics
list = list()

for i in range(3):
    list.append(float(input("Introduce una cifra: ")))

media = statistics.fmean(list)
mediana = statistics.median(list)
varianza = statistics.variance(list)

print("List: ", list)
print("Media: ", media)
print("Mediana: ", mediana)
print("Varianza: ", varianza)