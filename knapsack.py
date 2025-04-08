from typing import List, Tuple  # Import Tuple and List for type hints


def backpack_pd(n: int, c: int, itens) -> int:
    maxTab = [[0] * (c + 1) for _ in range(n + 1)]
    iteracoes = 0
    instrucoes = 0

    # Tupla (weight, value)
    # item[i][0] = peso do item i
    # item[i][1] = valor do item i
    
    i=1
    while i <= n:
        j=1
        while j <= c:
            iteracoes += 1
            if itens[i-1][0] <= j:
                maxTab[i][j] = max(maxTab[i - 1][j], itens[i-1][1] + maxTab[i - 1][j - itens[i-1][0]])
                instrucoes += 3 # Condicional + max + atribuição
            else:
                maxTab[i][j] = maxTab[i - 1][j]
                instrucoes += 2  # Condicional + atribuição
            j += 1
        i += 1

    # for row in maxTab:
    #     print(row)
    print(f"Iterações: {iteracoes}")
    print(f"Instruções: {instrucoes}")

    return maxTab[n][c]  # Retorna o valor máximo que pode ser obtido com a mochila de capacidade c

def ex1():
    # Exemplo 1
    n = 10
    c = 165
    itens = [(23, 92), (31, 57), (29, 49), (44, 68), (53, 60), (38, 43), (63, 67), (85, 84), (89, 87), (82, 72)]
    print(f'Valor: {backpack_pd(n, c, itens)}') # Saída esperada: 309

def ex2():
    # Exemplo 2
    n = 6
    c = 190
    itens = [(56, 50), (59, 50), (80, 64), (64, 46), (75, 50), (17, 5)]
    print(f'Valor: {backpack_pd(n, c, itens)}') # Saída esperada: 164

def main():
    ex1()
    ex2()

main() 