import math

def distancia_euclidiana(ponto1, ponto2):
    """
    Calcula a distancia euclidiana entre dois pontos
    """
    x1, y1 = ponto1
    x2, y2 = ponto2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def encontrar_coordenada_mais_proxima(pontos, ponto_referencia):
    """
    Encontra o par de coordenadas mais proximo a partir de um ponto de referencia pela busca par a par
    """
    distancia_minima = float('inf')
    coordenada_mais_proxima = None

    for ponto in pontos:
        distancia = distancia_euclidiana(ponto, ponto_referencia)
        if distancia < distancia_minima:
            distancia_minima = distancia
            coordenada_mais_proxima = ponto

    return coordenada_mais_proxima

# Exemplo de uso:
ponto_referencia = (0, 0)
coordenadas = [(1, 2), (1, 0), (-1, -1), (5, 6)]

coordenada_mais_proxima = encontrar_coordenada_mais_proxima(coordenadas, ponto_referencia)

print("O par de coordenadas mais proximo a", ponto_referencia, "eh", coordenada_mais_proxima)