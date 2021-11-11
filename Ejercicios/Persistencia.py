"""files example"""
f_o = open("archivo.data","w")
f_o.write("Texto para guardar 1\n")
f_o.write("Texto para guardar 2")
f_o.close()

f_o = open("archivo.data","r")
contenido = f_o.read()
print("\nContenido archivo: \n", contenido)
f_o.close()