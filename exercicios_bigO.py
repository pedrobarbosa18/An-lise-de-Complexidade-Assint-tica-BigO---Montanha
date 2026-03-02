# exercicios_bigO.py
# Disciplina: Estruturas de Dados e Análise de Algoritmos
# Aula 03 - Notação Assintótica
# Professor: Alexandre de Oliveira

# -------------------------------------------------------------------
# Exercício 1 - O(1)
# -------------------------------------------------------------------
def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]


# -------------------------------------------------------------------
# Exercício 2 - O(n)
# -------------------------------------------------------------------
def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total


# -------------------------------------------------------------------
# Exercício 3 - O(log n)
# -------------------------------------------------------------------
def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1


# -------------------------------------------------------------------
# Exercício 4 - O(n²)
# -------------------------------------------------------------------
def pares_com_soma(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                print(lista[i], lista[j])


# -------------------------------------------------------------------
# Exercício 5 - O(n²)
# -------------------------------------------------------------------
def imprimir_pares_e_soma(lista):
    # Bloco 1: imprime cada elemento
    for i in range(len(lista)):
        print(lista[i])

    # Bloco 2: imprime todos os pares
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])


# -------------------------------------------------------------------
# Exercício 6 - O(log n)
# -------------------------------------------------------------------
def potencias_de_dois(n):
    i = 1
    while i < n:
        print(i)
        i *= 2


# -------------------------------------------------------------------
# Exercício 7 - O(2^n)
# -------------------------------------------------------------------
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)


# -------------------------------------------------------------------
# Exercício 8 - O(n²)
# -------------------------------------------------------------------
def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


# -------------------------------------------------------------------
# Exercício 9 - O(n³)
# -------------------------------------------------------------------
def produto_de_matrizes(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C


# -------------------------------------------------------------------
# Exercício 10 - O(n log n)
# -------------------------------------------------------------------
def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado


# -------------------------------------------------------------------
# Testes rápidos
# -------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Ex1 ===", verificar_primeiro([10, 20, 30]))
    print("=== Ex2 ===", somar_lista([1, 2, 3, 4, 5]))
    print("=== Ex3 ===", busca_binaria([1, 3, 5, 7, 9], 7))
    print("=== Ex4 ==="); pares_com_soma([1, 2, 3, 4, 5], 6)
    print("=== Ex6 ==="); potencias_de_dois(16)
    print("=== Ex7 ===", fibonacci_recursivo(8))
    print("=== Ex8 ===", ordenacao_bolha([64, 34, 25, 12, 22]))
    print("=== Ex10 ===", merge_sort([38, 27, 43, 3, 9, 82, 10]))
