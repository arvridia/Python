import math
import math
import datetime

start_time = datetime.datetime.now()

x = 0
for i in range(1000):
   x += i

def distancia_euclidiana(ponto1, ponto2):
    """
    Calcula a distancia euclidiana entre dois pontos
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def encontrar_coordenada_mais_proxima_div_conq(coordenadas, ponto_referencia):
    """
    Encontra a coordenada mais proxima em relacao a um ponto de referencia usando divisao e conquista com pig back
    """
    def encontrar_coordenada_mais_proxima_rec(coordenadas):
        n = len(coordenadas)

        if n <= 1:
            return coordenadas[0] if n == 1 else None

        if n == 2:
            return min(coordenadas, key=lambda coord: distancia_euclidiana(coord, ponto_referencia))

        meio = n // 2
        coordenadas_esquerda = coordenadas[:meio]
        coordenadas_direita = coordenadas[meio:]

        coordenada_mais_proxima_esquerda = encontrar_coordenada_mais_proxima_rec(coordenadas_esquerda)
        coordenada_mais_proxima_direita = encontrar_coordenada_mais_proxima_rec(coordenadas_direita)

        distancia_esquerda = (
            distancia_euclidiana(coordenada_mais_proxima_esquerda, ponto_referencia)
            if coordenada_mais_proxima_esquerda is not None
            else float("inf")
        )

        distancia_direita = (
            distancia_euclidiana(coordenada_mais_proxima_direita, ponto_referencia)
            if coordenada_mais_proxima_direita is not None
            else float("inf")
        )

        if distancia_esquerda < distancia_direita:
            coordenada_mais_proxima = coordenada_mais_proxima_esquerda
            distancia_minima = distancia_esquerda
        else:
            coordenada_mais_proxima = coordenada_mais_proxima_direita
            distancia_minima = distancia_direita

        coordenadas_faixa = [
            coord for coord in coordenadas if abs(coord[0] - ponto_referencia[0]) < distancia_minima
        ]

        coordenadas_faixa.sort(key=lambda coord: coord[1])

        for i in range(len(coordenadas_faixa)):
            j = i + 1
            while j < len(coordenadas_faixa) and coordenadas_faixa[j][1] - coordenadas_faixa[i][1] < distancia_minima:
                distancia_ij = distancia_euclidiana(coordenadas_faixa[i], coordenadas_faixa[j])
                if distancia_ij < distancia_minima:
                    distancia_minima = distancia_ij
                    coordenada_mais_proxima = coordenadas_faixa[i]
                j += 1

        return coordenada_mais_proxima

    coordenadas_ordenadas_x = sorted(coordenadas, key=lambda coord: coord[0])
    return encontrar_coordenada_mais_proxima_rec(coordenadas_ordenadas_x)

# Exemplo de uso:
coordenadas = [(1, 2), (3, 4), (-1, -1), (5, 6),(1, 2), (3, 4), (-1, -1), (5, 6),(1, 2), (3, 4), (-1, -1), (5, 6),(1, 2), (3, 4), (-1, -1), (5, 6),(1, 2), (3, 4), (-1, -1), (5, 6)]
ponto_referencia = (0, 0)

coordenada_mais_proxima = encontrar_coordenada_mais_proxima_div_conq(coordenadas, ponto_referencia)

print("A coordenada mais proxima em relacao a", ponto_referencia, "eh", coordenada_mais_proxima)

end_time = datetime.datetime.now()

time_diff = (end_time - start_time)
execution_time = time_diff.total_seconds() * 1000000

print(execution_time)