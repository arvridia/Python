from collections import defaultdict
import itertools

class solucionador:
    def __init__(self, n):
        self.n = n
        self.graph = defaultdict(list)
        self.visited = [False] * (2 * n)
        self.stack = []

    def add_clause(self, u, v):
        self.graph[-u].append(v)
        self.graph[-v].append(u)

    def dfs(self, u):
        self.visited[u] = True
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs(v)
        self.stack.append(u)

    def scc(self):
        scc_result = [-1] * (2 * self.n)
        scc_count = 0
        for i in range(1, 2 * self.n):
            if not self.visited[i]:
                self.dfs(i)
        reversed_graph = defaultdict(list)
        for u in self.graph:
            for v in self.graph[u]:
                reversed_graph[v].append(u)
        while self.stack:
            u = self.stack.pop()
            if scc_result[u] == -1:
                self.dfs_scc(u, scc_count, reversed_graph, scc_result)
                scc_count += 1
        for i in range(1, self.n):
            if scc_result[i] == scc_result[-i]:
                return None
        atribuicao = [(i < self.n) ^ (scc_result[i] > scc_result[-i]) for i in range(1, self.n + 1)]
        return atribuicao

    def dfs_scc(self, u, scc_count, reversed_graph, scc_result):
        self.visited[u] = False
        scc_result[u] = scc_count
        for v in reversed_graph[u]:
            if self.visited[v]:
                self.dfs_scc(v, scc_count, reversed_graph, scc_result)

def solucao_2sat(clausulas, n):
    solucao = solucionador(n)
    for clausula in clausulas:
        u, v = clausula
        solucao.add_clause(u, v)
    return solucao.scc()

if __name__ == "__main__":
    n = 3
    clausulas = [(1, 2), (-1, 3), (-2, -3)]
    atribuicao = solucao_2sat(clausulas, n)
    if atribuicao is None:
        print("Sem atribuicoes satisfatorias!")
    else:
        print("Atribuicao satisfatoria encontrada:")
        for i, valor in enumerate(atribuicao, start=1):
            print(f"Variavel {i}: {valor}")
