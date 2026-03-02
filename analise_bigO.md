# Análise de Complexidade Assintótica (Big-O)

**Disciplina:** Estruturas de Dados e Análise de Algoritmos  
**Aula:** 03 – Notação Assintótica  
**Data:** 02/03/2026  
**Professor:** Alexandre de Oliveira  

---

## Exercício 1 – `verificar_primeiro`

```python
def verificar_primeiro(lista):
    if len(lista) == 0:
        return None
    return lista[0]
```

**Complexidade:** O(1)

**Justificativa:** A função executa apenas operações de tempo constante: verifica o tamanho da lista e acessa diretamente o primeiro elemento pelo índice. Não há loops nem recursão, portanto o tempo de execução não cresce com o tamanho da entrada.

---

## Exercício 2 – `somar_lista`

```python
def somar_lista(lista):
    total = 0
    for elemento in lista:
        total += elemento
    return total
```

**Complexidade:** O(n)

**Justificativa:** Há um único `for` que percorre todos os `n` elementos da lista uma vez. A operação dentro do loop é O(1), resultando em tempo linear proporcional ao tamanho da entrada.

---

## Exercício 3 – `busca_binaria`

```python
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
```

**Complexidade:** O(log n)

**Justificativa:** A cada iteração do `while`, o espaço de busca é dividido ao meio. No pior caso, o número de iterações é log₂(n). Por isso, o tempo cresce logaritmicamente em relação ao tamanho da lista.

---

## Exercício 4 – `pares_com_soma`

```python
def pares_com_soma(lista, alvo):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == alvo:
                print(lista[i], lista[j])
```

**Complexidade:** O(n²)

**Justificativa:** Há dois loops aninhados. O loop externo itera `n` vezes e o interno itera até `n-1` vezes. O número total de comparações é aproximadamente n*(n-1)/2, que é O(n²).

---

## Exercício 5 – `imprimir_pares_e_soma`

```python
def imprimir_pares_e_soma(lista):
    # Bloco 1: imprime cada elemento
    for i in range(len(lista)):
        print(lista[i])

    # Bloco 2: imprime todos os pares
    for i in range(len(lista)):
        for j in range(len(lista)):
            print(lista[i], lista[j])
```

**Complexidade:** O(n²)

**Justificativa:** O Bloco 1 é O(n) e o Bloco 2 possui dois loops aninhados, sendo O(n²). Como O(n²) domina O(n), a complexidade total é O(n²). Em notação assintótica, mantemos apenas o termo de maior crescimento.

---

## Exercício 6 – `potencias_de_dois`

```python
def potencias_de_dois(n):
    i = 1
    while i < n:
        print(i)
        i *= 2
```

**Complexidade:** O(log n)

**Justificativa:** A variável `i` é multiplicada por 2 a cada iteração, dobrando de valor. Para atingir `n`, são necessárias log₂(n) iterações. O crescimento do tempo é, portanto, logarítmico.

---

## Exercício 7 – `fibonacci_recursivo`

```python
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
```

**Complexidade:** O(2ⁿ)

**Justificativa:** Cada chamada gera duas novas chamadas recursivas, formando uma árvore binária de chamadas. A profundidade da árvore é `n`, resultando em aproximadamente 2ⁿ chamadas no pior caso. Não há memoização, então subproblemas são recalculados repetidamente.

---

## Exercício 8 – `ordenacao_bolha` (Bubble Sort)

```python
def ordenacao_bolha(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista
```

**Complexidade:** O(n²)

**Justificativa:** Existem dois loops aninhados: o externo itera `n` vezes e o interno itera `n - i - 1` vezes. O total de comparações é n*(n-1)/2, que é O(n²). Essa é a complexidade característica do algoritmo Bubble Sort no pior caso.

---

## Exercício 9 – `produto_de_matrizes`

```python
def produto_de_matrizes(A, B, n):
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C
```

**Complexidade:** O(n³)

**Justificativa:** Três loops aninhados, cada um iterando `n` vezes sobre as dimensões da matriz. A operação dentro do loop mais interno é O(1), resultando em n × n × n = n³ operações totais.

---

## Exercício 10 – `merge_sort`

```python
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
```

**Complexidade:** O(n log n)

**Justificativa:** O algoritmo divide recursivamente a lista ao meio (log n divisões) e, em cada nível da recursão, realiza a etapa de merge que percorre todos os `n` elementos. Combinando: log n níveis × n operações por nível = O(n log n).

---

## Tabela Resumo

| Exercício | Função                  | Complexidade |
|-----------|-------------------------|--------------|
| 1         | `verificar_primeiro`    | O(1)         |
| 2         | `somar_lista`           | O(n)         |
| 3         | `busca_binaria`         | O(log n)     |
| 4         | `pares_com_soma`        | O(n²)        |
| 5         | `imprimir_pares_e_soma` | O(n²)        |
| 6         | `potencias_de_dois`     | O(log n)     |
| 7         | `fibonacci_recursivo`   | O(2ⁿ)        |
| 8         | `ordenacao_bolha`       | O(n²)        |
| 9         | `produto_de_matrizes`   | O(n³)        |
| 10        | `merge_sort`            | O(n log n)   |

---

> **Repositório GitHub:** _[inserir link aqui após criar o repositório]_
