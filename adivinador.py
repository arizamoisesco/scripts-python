import random

def pregunta_numero():
    while True:
        numero_usuario = input("> ")

        if numero_usuario.isdecimal():
            return int(numero_usuario)
        
        print("Por favor ingrese un numero entre 1 y 100")

print("Adivina un número")
print()
numero_secreto = random.randint(1,100)
print("Estoy pensando un número entre 1 y 100")

for numero_intento in range(10):
    print(f"Tienes {10 - numero_intento} intentos")

    numero_usuario = pregunta_numero()

    if numero_usuario == numero_secreto:
        break #Rompe el ciclo

    #Pistas para el usuario
    if(numero_usuario < numero_secreto):
        print("Tu numero es muy bajo")
    elif(numero_usuario > numero_secreto):
        print("Tu numero es muy alto")

#Revelar el resultado
if numero_usuario == numero_secreto:
    print("felicidades adivinaste el número")
else:
    print("Juego terminado el número que pense fue: ",numero_secreto)
    
