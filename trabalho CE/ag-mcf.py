import random
import numpy as np

def simulacao_rede(lambdas, mus, Tmax=10**3):
    num_cruzamentos = len(lambdas)
    filas = [[] for _ in range(num_cruzamentos)]  # Inicializa as filas vazias
    tempos = [0]  # Lista para armazenar os tempos de eventos

    infos = []  # Lista para armazenar informações sobre os eventos

    # Inicializa o tempo atual
    tempo_atual = 0

    # Loop principal da simulação
    while tempo_atual < Tmax:
        # Calcula as taxas de chegada e saída para cada cruzamento
        taxas_chegada = lambdas
        taxas_saida = mus
        
        # Calcula as probabilidades de cada evento acontecer
        probabilidades = np.array(taxas_chegada + taxas_saida, dtype=np.float64)
        probabilidades /= np.sum(probabilidades)
        
        # Escolhe um evento aleatoriamente com base nas probabilidades
        evento = random.choices(['chegada'] * num_cruzamentos + ['saida'] * num_cruzamentos, probabilidades)[0]

        # Lida com eventos de chegada
        if evento == 'chegada':
            cruzamento = random.randrange(num_cruzamentos)  # Escolhe um cruzamento aleatoriamente
            tempo_chegada = np.random.exponential(1 / lambdas[cruzamento])
            tempo_atual += tempo_chegada
            filas[cruzamento].append(tempo_atual)
            infos.append(('chegada', cruzamento, tempo_atual))

        # Lida com eventos de saída
        else:
            cruzamento = random.randrange(num_cruzamentos)  # Escolhe um cruzamento aleatoriamente
            if filas[cruzamento]:  # Se houver carros na fila
                tempo_atendimento = np.random.exponential(1 / mus[cruzamento])
                tempo_atual += tempo_atendimento
                filas[cruzamento].pop(0)  # Remove o carro atendido da fila
                infos.append(('saida', cruzamento, tempo_atual))

        # Atualiza o tempo atual
        tempos.append(tempo_atual)

    return tempos, infos, filas

def tempo_medio_espera(infos, num_cruzamentos):
    tempo_espera = [0] * num_cruzamentos
    qtd_chegadas = [0] * num_cruzamentos
    tempo_chegada = [0] * num_cruzamentos  # Armazena o tempo de chegada do último veículo em cada cruzamento

    for evento in infos:
        if evento[0] == 'saida':
            cruzamento = evento[1]
            tempo_saida = evento[2]
            tempo_espera[cruzamento] += tempo_saida - tempo_chegada[cruzamento]  # Calcula o tempo de espera
            qtd_chegadas[cruzamento] += 1
        elif evento[0] == 'chegada':
            cruzamento = evento[1]
            tempo_chegada[cruzamento] = evento[2]  # Atualiza o tempo de chegada

    return [tempo_espera[i] / qtd_chegadas[i] if qtd_chegadas[i] != 0 else 0 for i in range(num_cruzamentos)]


# Definição dos parâmetros
lambdas = [10, 27, 25, 30, 7]  # Taxas de chegada para cada cruzamento
mus = [15, 30, 24, 20, 6]  # Taxas de saída para cada cruzamento

# Realiza a simulação e calcula o tempo médio de espera para cada cruzamento
resultados = {}
for i in range(len(lambdas)):
    mus_modificado = mus.copy()
    mus_modificado[i] += 5  # Aumenta a taxa de saída em 5 para cada cruzamento
    tempos, infos, _ = simulacao_rede(lambdas, mus_modificado)
    resultados[f'Cruzamento {chr(65 + i)}'] = tempo_medio_espera(infos, len(lambdas))

# Imprime os resultados
print("Tempo médio de espera em cada cruzamento:")
for cruzamento, tempos_medios in resultados.items():
    print(f"{cruzamento}: {np.mean(tempos_medios):.2f} minutos")
