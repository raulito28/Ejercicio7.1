import persistencia_json
import json
lista_coches = json.load(open("Coches.txt", "r"))
json.dump(json.dumps(lista_coches), open("Coches.txt", "w"))
lista_coches = []
print("\nLista coches:\n", lista_coches)
lista_coches = json.loads(json.load(open("Coches.txt", "r")))
print("\nLista coches:\n", lista_coches)