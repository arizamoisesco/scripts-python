X_REPETIR = 19
Y_REPETIR = 12

#Anidación de ciclos
for y in range(Y_REPETIR):
    for x in range(X_REPETIR):
        print("/ \_", end="")
    print()

    for x in range(X_REPETIR):
        print("\_/ ", end="")
    print()