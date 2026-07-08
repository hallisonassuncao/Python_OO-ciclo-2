def potencia(base, expoente):
    resultado = 1
    if expoente == 0:
        return 1

    for _ in range(expoente):
        resultado *= base
    return resultado


def ler_valores():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    return x, y


def main():
    x, y = ler_valores()

    resultado = potencia(x, y)

    print(f"\nResultado de {x}^{y} = {resultado}")


if __name__ == "__main__":
    main()