def mostrar_multiplos(x):
    print(f"\nMúltiplos de {x} entre 1 e 100:")
    for i in range(1, 101):
        if i % x == 0:
            print(i)


def main():
    x = int(input("Digite um número: "))

    if x == 0:
        print("Não é possível calcular múltiplos de zero.")
    else:
        mostrar_multiplos(x)


if __name__ == "__main__":
    main()