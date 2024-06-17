from itertools import product
import sys
import time

start = time.time()

class programa:
    def powerset_with_negatives(vetor):
        for p in product([-1, 1], repeat=len(vetor)):
            yield [x * y for x, y in zip(vetor, p)]

    if __name__ == "__main__":
        
        # Exemplo de uso:
        vetor_exemplo = [1, 2, 1, 3]

        resultado = list(powerset_with_negatives(vetor_exemplo))

        #Exemplo de alvo
        k = 1

        print('\nSomas:')
        for i in resultado:
            if sum(i) == k:
                print(i)

end = time.time()
print('\nTempo gasto: ')
print(end - start)  


