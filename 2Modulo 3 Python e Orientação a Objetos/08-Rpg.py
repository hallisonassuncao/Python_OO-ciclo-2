class Personagem:
    def __init__(self, nome, nivel):
        self._nome = nome
        self._nivel = nivel

    def atacar(self):
        print(f"\n{self._nome} realiza um ataque.")


class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.__forca = forca

    def atacar(self):
        print(f"\n{self._nome} realiza um ataque físico! (Força: {self.__forca}).")


def main():
    personagem = Personagem("Jaspion", 7)
    guerreiro = Guerreiro("Hulk", 8, 81)

    lista_personagens = [personagem, guerreiro]

    print("\n--- Ataques dos Guerreiros ---")
    for p in lista_personagens:
        p.atacar()


if __name__ == "__main__":
    main()