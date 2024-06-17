from collections import defaultdict

class Solucionador2SAT:
    def __init__(self, n):
        self.n = n
        self.grafo = defaultdict(list)
        self.visitado = [False] * (2 * n)
        self.pilha = []

    def adicionar_clausula(self, u, v):
        # Certifique-se de que u e v estejam na faixa correta com base na numeração das variáveis.
        # Se suas variáveis forem baseadas em 0, adicione 1 a u e v aqui.
        self.grafo[-u].append(v)
        self.grafo[-v].append(u)

    def dfs(self, u):
        self.visitado[u] = True
        for v in self.grafo[u]:
            if not self.visitado[v]:
                self.dfs(v)
        self.pilha.append(u)

    def scc(self):
        resultado_scc = [-1] * (2 * self.n)
        contador_scc = 0

        for i in range(1, 2 * self.n):
            if not self.visitado[i]:
                self.dfs(i)

        grafo_reverso = defaultdict(list)
        for u in self.grafo:
            for v in self.grafo[u]:
                grafo_reverso[v].append(u)

        while self.pilha:
            u = self.pilha.pop()
            if resultado_scc[u] == -1:
                self.dfs_scc(u, contador_scc, grafo_reverso, resultado_scc)
                contador_scc += 1

        for i in range(1, self.n):
            if resultado_scc[i] == resultado_scc[-i]:
                return None  # Sem atribuição satisfatória

        atribuicao = [(i <= self.n) ^ (resultado_scc[i] > resultado_scc[-i]) for i in range(1, self.n + 1)]
        return atribuicao

    def dfs_scc(self, u, contador_scc, grafo_reverso, resultado_scc):
        self.visitado[u] = False
        resultado_scc[u] = contador_scc
        for v in grafo_reverso[u]:
            if self.visitado[v]:
                self.dfs_scc(v, contador_scc, grafo_reverso, resultado_scc)

def resolver_2sat(clausulas, n):
    solucionador = Solucionador2SAT(n)
    for clausula in clausulas:
        u, v = clausula
        solucionador.adicionar_clausula(u, v)

    return solucionador.scc()

def main():
    n = 3  # Número de variáveis
    clausulas = [(1, 2), (-1, 3), (-2, -3)]

    atribuicao = resolver_2sat(clausulas, n)

    if atribuicao is None:
        print("Sem atribuição satisfatória.")
    else:
        print("Atribuição satisfatória:")
        for i, valor in enumerate(atribuicao, start=1):
            print(f"Variável {i}: {valor}")

if __name__ == "__main__":
    main()