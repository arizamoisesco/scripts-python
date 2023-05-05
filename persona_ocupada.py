#
while True:
    print("¿Te gustaria saber como tener a una persona ocupada? Si/No")
    respuesta = input("> ")
    if respuesta.lower() == "no" or respuesta.lower() == "n":
        break
    elif respuesta.lower() == "si" or respuesta.lower() == "s":
        continue 

print("Gracias, fue una broma, ten una bonita noche")