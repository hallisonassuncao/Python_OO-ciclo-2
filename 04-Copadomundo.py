from abc import ABC, abstractmethod

class ClubeParticipante(ABC):
    def __init__(self, nome, pais, confederacao, ranking_fifa, gols_marcados, vitorias):
        self. nome = nome
        self.pais = pais
        self.confederacao = confederacao
        self.ranking_fifa = ranking_fifa
        self.gols_marcados = gols_marcados
        self.vitorias = vitorias

    def exibir_dados(self):
        print(f"\nClube: {self.nome}")
        print(f"País: {self.pais}")
        print(f"Confederação: {self.confederacao}")
        print(f"Ranking FIFA: {self.ranking_fifa}")
        print(f"Vitórias: {self.vitorias}")
        print(f"Gols marcados: {self.gols_marcados}")

    @abstractmethod
    def calcular_desempenho(self):
        pass

    @abstractmethod
    def gerar_relatorio_tecnico(self):
        pass


class ClubeUEFA(ClubeParticipante):
    def calcular_desempenho(self):
        return (self.vitorias * 3) + (self.gols_marcados * 0.5)
    
    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        print(f"Desempenho: {desempenho:.2f}")


class ClubeCONMEBOL(ClubeParticipante):
    def calcular_desempenho(self):
        return (self.vitorias * 3) + (self.gols_marcados * 0.7)
    
    def gerar_relatorio_tecnico(self):
        self.exibir_dados()
        desempenho = self.calcular_desempenho()
        print(f"Desempenho: {desempenho:.2f}")


def main():
    Barcelona = ClubeUEFA("Barcelona", "Noruega", "UEFA", 1, 15, 6)
    Flamengo = ClubeCONMEBOL("Flamengo", "Brasil", "CONMEBOL", 8, 15, 5)

    clubes = [Barcelona, Flamengo]

    for clube in clubes:
        print("\n" + "-" * 40)
        clube.gerar_relatorio()

if __name__ == "__main__":
    main()