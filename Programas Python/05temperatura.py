temperatura = float(input("Digite a temperatura em °C: "))

if temperatura < 0:
    print("Frio extremo")
elif temperatura <= 10:
    print("Frio")
elif temperatura <= 25:
    print("Ameno")
elif temperatura <= 35:
    print("Quente")
else:
    print("Muito quente")