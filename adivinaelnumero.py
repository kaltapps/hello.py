numero_adivinar = input("Que numero quieres que adiviine tu compañero: ")

adivina_numero = input("Adivina el numero: ")

while numero_adivinar != adivina_numero:

    adivina_numero = input("Adivina el numero:")

    if adivina_numero == numero_adivinar:
        print("¡Has ganado!")
