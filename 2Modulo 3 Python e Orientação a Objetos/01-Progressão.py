class ProgressaoAritmetica:
    def __init__(self, n, a1, r):
        self.n = n
        self.a1 = a1
        self.r = r

    def calcular_termos(self):
        termos = []
        for i in range(self.n):
            termos.append(self.a1 + self.r * i)
        return termo

    def calcular_soma(self):
        an = self.a1 + self.r * (self.n - 1)
        return self.n * (self.a1 + an) / 2


def main():
    n = int(input("Digite o número de termos: "))
    a1 = float(input("Digite o primeiro termo: "))
    r = float(input("Digite a razão: "))

    pa = ProgressaoAritmetica(n, a1, r)

    print("\nTermos da P.A.:")
    for termo in pa.calcular_termos():
        print(termo)

    print(f"\nSoma dos elementos: {pa.calcular_soma()}")


if __name__ == "__main__":
    main()