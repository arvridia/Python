import time

start = time.time()

def target_sum_count(vetor, K):
    total_sum = sum(vetor)

    #Teste de paridade
    if (total_sum + K) % 2 != 0 or K > total_sum:
        return 0

    #Reduz possibilidades de conjuntos
    target_sum = (total_sum + K) // 2
    return subset_sum_count(vetor, target_sum)

def subset_sum_count(vetor, target_sum):
    n = len(vetor)

    #armazenar contagem
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]

    #base
    for i in range(n + 1):
        dp[i][0] = 1

    #Matriz de prog dinâmica
    for i in range(1, n + 1):
        for j in range(target_sum + 1):
            if vetor[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - vetor[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

#Exemplo de uso:
V = [1, 2, 1, 3]
K = 1
resultado = target_sum_count(V, K)

print(f'Número de maneiras diferentes: {resultado}')

end = time.time()
print('\nTempo gasto: ')
print(end - start)  
